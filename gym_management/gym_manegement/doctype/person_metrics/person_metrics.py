# Copyright (c) 2023, Gym and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class PersonMetrics(Document):
	def before_save(self):
		if self.height:
			self.bmi = (self.weight/(self.height * self.height))
