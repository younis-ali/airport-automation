# Copyright (c) 2024, Ambibuzz and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AirplaneFlight(Document):
	
	def on_submit(self):
		# Set the status to Completed
		self.status = "Completed"
