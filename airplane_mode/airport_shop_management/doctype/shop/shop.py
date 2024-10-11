# Copyright (c) 2024, Ambibuzz and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe import _

class Shop(WebsiteGenerator):
	def before_save(self):
		# Check if the status is being changed to 'Available'
		if self.status == "Available":
			# Clear tenant details and contract expiry fields
			self.tenant_details = None
			self.contract_expiry = None
			
			frappe.msgprint(_("Tenant details and contract expiry have been cleared because the shop is now available."), alert=True)