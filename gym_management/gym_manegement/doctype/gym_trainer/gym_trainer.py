# Copyright (c) 2023, Gym and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymTrainer(Document):
	# set the full name of member based on their first and last names
	def set_full_name(self):
		if self.last_name:
			self.full_name = " ".join(filter(None, [self.first_name, self.last_name]))
		else:
			self.full_name = self.first_name
	# create a new user based on the trainer settings 
	def create_website_user(self):
		users = frappe.db.get_all(
			"User",
			fields=["email"],
			or_filters={"email": self.email},
		)
		if users and users[0]:
			frappe.throw(
				_(
					"User exists with Email {}, Mobile {}<br>Please check email / mobile or disable 'Invite as User' to skip creating User"
				).format(frappe.bold(users[0].email)),
				frappe.DuplicateEntryError,
			)

		user = frappe.get_doc(
			{
				"doctype": "User",
				"first_name": self.first_name,
				"last_name": self.last_name,
				"email": self.email,
				"user_type": "Website User",
				"gender": self.gender,
				"phone": self.phone_number,
				"gender": self.gender,
				"birth_date": self.dob,
			}
		)
		user.flags.ignore_permissions = True
		user.enabled = True
		user.send_welcome_email = False
		user.add_roles("Gym Trainer")
		self.db_set("user_id", user.name)

    # create a frappe user if requested
	def on_update(self):
		if not self.user_id and self.email and self.invite_user:
			self.create_website_user()
