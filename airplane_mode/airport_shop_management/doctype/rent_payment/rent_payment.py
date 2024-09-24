# Copyright (c) 2024, Ambibuzz and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RentPayment(Document):
	def before_insert(self):
		# Automatically generate a unique receipt number before inserting
		self.receipt_number = frappe.generate_hash(self.name, 10)