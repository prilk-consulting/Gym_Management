from __future__ import unicode_literals

import frappe

def get_context(context):
	if frappe.session.user == "Guest":
		frappe.throw(("You need to be logged in to access this page"), frappe.PermissionError)

	context.show_sidebar = True
	
	if frappe.db.exists("Person", {"email": frappe.session.user}):
		member = frappe.get_doc("Person", {"email": frappe.session.user})
		frappe.form_dict.new = 0
		frappe.form_dict.name = member.name
		
	else:
		frappe.throw(("Member not found, please contact Gym Administration"), frappe.PermissionError)
