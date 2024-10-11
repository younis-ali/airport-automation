# Copyright (c) 2024, Ambibuzz and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate
from datetime import timedelta


class Contract(Document):
	def validate(self):
		# Validate contract dates
		if self.contract_start and self.contract_end:
			contract_start_date = getdate(self.contract_start)
			contract_end_date = getdate(self.contract_end)
			
			# Ensure contract_end is at least one year after contract_start
			if contract_end_date < contract_start_date + timedelta(days=365):
				frappe.throw(
					_("Contract End Date must be at least one year after the Contract Start Date."),
					title=_("Invalid Contract Dates")
				)
		
		# Validate Shop status
		if self.shop:
			shop_doc = frappe.get_doc("Shop", self.shop)  # Fetch the linked Shop document
			# Check if the shop status is 'Leased'
			if shop_doc.status == "Leased":
				frappe.throw(
					_("Shop {0} is already leased and cannot be contracted.").format(shop_doc.shop_name),
					title=_("Shop Leased")
				)

	def after_insert(self):
		# Change the shop status to 'Leased' once the tenant contract is created
		if self.shop:
			shop_doc = frappe.get_doc("Shop", self.shop)
			shop_doc.status = "Leased"
			shop_doc.tenant_details = self.tenant
			shop_doc.contract_expiry = self.contract_end

			shop_doc.save(ignore_permissions=True)  # Save the changes to the Shop document

			frappe.msgprint(_("Shop {0} has been marked as 'Leased'.").format(shop_doc.shop_name), alert=True)

