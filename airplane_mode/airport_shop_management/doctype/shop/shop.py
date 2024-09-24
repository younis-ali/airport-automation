# Copyright (c) 2024, Ambibuzz and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Shop(Document):
	def before_insert(self):
		# self.monthly_rent = 845748.4
		start_date = getdate(self.lease_start_date)
		end_date = getdate(self.lease_expiry_date)

		if start_date >= end_date:
			frappe.throw("Lease end date should be after lease start date")
		
		lease_duration = relativedelta(end_date, start_date)
		total_months = lease_duration.years * 12 + lease_duration.months

		if total_months > 0:
			self.monthly_rent = self.rent_amount / total_months
		else:
			frappe.throw("Lease duration cannot be zero or negative")
