# Copyright (c) 2024, Ambibuzz and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
	
	# Implement the before_save controller hook 
	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name}"	
