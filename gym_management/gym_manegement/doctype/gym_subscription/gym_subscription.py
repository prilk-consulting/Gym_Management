# Copyright (c) 2023, Gym and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class GymSubscription(WebsiteGenerator):
	def before_save(self):
		if not self.route:
			self.route = f"/{self.name}"
