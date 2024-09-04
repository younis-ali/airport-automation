# Copyright (c) 2024, Ambibuzz and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

import random
import string


class AirplaneTicket(Document):
	
	# Implement the controller to compute total amount
	def before_save(self):

		add_on_amount = 0
		# Iterate through the child table and compute total amount
		for add_on in self.add_ons:
			add_on_amount = add_on_amount+add_on.amount

		# set the total amount field
		self.total_amount = self.flight_price + add_on_amount

	# Validate to avoid duplicate add-ons

	def validate(self):
		# Dictionary to keep track of unique add-ons
		unique_add_ons = {}
		removed_add_ons = []

		# Create a list of items to be removed
		items_to_remove = []

		# Iterate over the add_ons child table to find duplicates
		for add_on in self.add_ons:
			add_on_item = add_on.item 
			if add_on_item in unique_add_ons:
				# Duplicate found, add to the removal list
				removed_add_ons.append(add_on_item)
				items_to_remove.append(add_on)
			else:
				# Add the unique add-on to the dictionary
				unique_add_ons[add_on_item] = add_on.amount

		# Remove the duplicates after iteration
		for item in items_to_remove:
			self.remove(item)

		# If any duplicates found and removed give message to the user
		if removed_add_ons:
			frappe.msgprint(
				f"You can't have one add-on more then once. Removing: {', '.join(removed_add_ons)}",
				alert=True
			)
	
	# implement the before_submit controller hook

	def before_submit(self):
		if self.status != 'Boarded':
			frappe.throw(f"The Airplane Ticket cannot be submitted because the status is '{self.status}'. Please ensure the status is 'Boarded' before submitting.")

	# implement the controller hook to set the seat

	def before_insert(self):
		random_int = random.randint(1,99)
		random_char = random.choice('ABCDE')
		self.seat = f"{random_int}{random_char}"

# bench --site frappe.fullstack execute airplane_mode.airplane_mode.doctype.airplane_ticket.airplane_ticket.test
def test():
	obj = frappe.get_doc({
		'doctype': 'Airplane Ticket',
	})

	obj.before_save()