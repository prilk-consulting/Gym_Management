# Copyright (c) 2023, Gym and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import getdate, date_diff
from frappe.model.document import Document

class GMembership(Document):
	
	@property
	def membership_status(self):
		return get_membership_status(self.start_date, self.end_date)

	@property
	def days_left(self):
		return get_days_left(self.end_date)

@frappe.whitelist()
def get_membership_status(start_date, end_date):
	today = getdate()
	end   = getdate(end_date)
	start = getdate(start_date)
	if end < today:
		return "Expired"
	elif start > today:
		return "Not Started"
	else:
		return "Active"

@frappe.whitelist()
def get_days_left(end_date):
	if end_date:
		today = getdate()
		end   = getdate(end_date)
		days_left = days_left(end, today)
	else:
		return 0

	if days_left < 0:
		return 0
	else:
		return days_left