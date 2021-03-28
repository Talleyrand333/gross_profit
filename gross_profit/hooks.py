# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "gross_profit"
app_title = "Gross Profit"
app_publisher = "Akeru Ebuka"
app_description = "Modification made to the gross profit report"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ebukaakeru@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gross_profit/css/gross_profit.css"
# app_include_js = "/assets/gross_profit/js/gross_profit.js"

# include js, css files in header of web template
# web_include_css = "/assets/gross_profit/css/gross_profit.css"
# web_include_js = "/assets/gross_profit/js/gross_profit.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "gross_profit.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "gross_profit.install.before_install"
# after_install = "gross_profit.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gross_profit.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"gross_profit.tasks.all"
# 	],
# 	"daily": [
# 		"gross_profit.tasks.daily"
# 	],
# 	"hourly": [
# 		"gross_profit.tasks.hourly"
# 	],
# 	"weekly": [
# 		"gross_profit.tasks.weekly"
# 	]
# 	"monthly": [
# 		"gross_profit.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "gross_profit.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "gross_profit.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "gross_profit.task.get_dashboard_data"
# }

