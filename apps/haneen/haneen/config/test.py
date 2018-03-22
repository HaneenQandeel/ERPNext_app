from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("School Information"),
			"items": [
				{
					"type": "doctype",
					"name": "School",
					"description": _("School records."),
				},
				{
					"type": "doctype",
					"name": "Class",
					"description": _("Class records."),
				}
				
			]
		}

	]
