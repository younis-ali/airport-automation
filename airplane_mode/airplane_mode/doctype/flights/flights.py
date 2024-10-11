# Copyright (c) 2024, Ambibuzz and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Flights(WebsiteGenerator):
	def on_submit(self):
		self.status='Completed'
	
	def on_cancle(self):
		self.status='Cancelled'

def sync_gate_number(doc, method):
	updated_gate_number = doc.gate_number

	# Find all Airplane Ticket documents linked to the flight
	tickets = frappe.get_all("Airplane Ticket", filters={"flight": doc.name}, fields=["name"])

	for ticket in tickets:
		# Load the Airplane Ticket document
		ticket_doc = frappe.get_doc("Airplane Ticket", ticket["name"])
		
		# Update the gate_number and save the ticket
		ticket_doc.gate_number = updated_gate_number
		ticket_doc.save()

	frappe.msgprint(f"Gate number updated in all linked tickets for flight {doc.name}.")