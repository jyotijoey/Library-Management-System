# Copyright (c) 2023, jyoti burnwal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Transaction(Document):
	def after_insert(doc):
		member =frappe.get_doc("Member", doc.member)
		book_price = frappe.db.get_value("Book", doc.book, "price")
		member.amount_due = member.amount_due + book_price
		member.save(ignore_permissions = True)
