# Copyright (c) 2024, Ambibuzz and contributors
# For license information, please see license.txt

import frappe

def get_cols():
	return [
		{
			"fieldname" : "airline",
			"label" : "Airline",
			"fieldtype" : "Link",
			"options" : "Airline",
			"width" : "110"
		},
		{
			"fieldname" : "revenue",
			"label" : "Revenue",
			"fieldtype" : "Currency",
			"width" : "110"
		}
	]

# bench --site frappe.fullstack execute airplane_mode.airplane_mode.report.revenue_by_airline.revenue_by_airline.get_data
def get_data():
	# Fetch all airlines
	airlines = frappe.get_all("Airline", fields=["name"])

	data = []

	for airline in airlines:
		# Calculate the total revenue per airline, including add-ons
		revenue = frappe.db.sql("""
			SELECT SUM(t.flight_price + IFNULL(ai.total_addon_amount, 0)) AS total_revenue
			FROM `tabAirplane Ticket` t
			JOIN `tabFlights` f ON t.flight = f.name
			JOIN `tabAirplane` a ON f.airplane = a.name
			LEFT JOIN (
				SELECT parent, SUM(amount) AS total_addon_amount
				FROM `tabAirplane Ticket Add-on Item`
				GROUP BY parent
			) ai ON t.name = ai.parent
			WHERE a.airline = %s
		""", (airline.name), as_list=True)[0][0] or 0.0

		# Append the airline and its revenue
		data.append([airline.name, revenue])
	return data

def get_chart_data(data):
	labels = [row[0] for row in data]  # Airline names
	values = [row[1] for row in data]  # Revenue values

	chart = {
		"data": {
			"labels": labels,
			"datasets": [
				{
					"name": "Revenue",
					"values": values
				}
			]
		},
		"type": "donut"
	}
	return chart

def execute(filters=None):
	columns = get_cols()
	data = get_data()
	chart = get_chart_data(data)
	total_revenue = sum(row[1] for row in data)
	data.append(["Total Revenue", total_revenue])

	# Include a summary row for total revenue
	summary = [
		{'label': 'Total Revenue', 'value': frappe.format_value(total_revenue, 'Currency')}
	]

	return columns, data, None, chart, summary
