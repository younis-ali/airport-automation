# Copyright (c) 2024, Ambibuzz and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import validate_email_address


class Tenant(Document):
	def validate(self):
		if self.email:
			if not validate_email_address(self.email):
				frappe.throw(f"Invalid email address : {self.email}")
