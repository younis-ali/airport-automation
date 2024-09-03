# Copyright (c) 2024, Ambibuzz and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):
	
	# Implement the controller to compute total amount
	def before_save(self):

		add_on_amount = 0
		# Iterate through the child table and compute total amount
		for add_on in self.add_ons:
			add_on_amount = add_on_amount+add_on.amount

		# set the total amount field
		self.total_amount = self.flight_price + add_on_amount


# bench --site frappe.fullstack execute airplane_mode.airplane_mode.doctype.airplane_ticket.airplane_ticket.test
def test():
	obj = frappe.get_doc({
		'doctype': 'Airplane Ticket',
	})

	obj.before_save()