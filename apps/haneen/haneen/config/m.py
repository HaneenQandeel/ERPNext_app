from __future__ import unicode_literals
from frappe import _



def get_data():
	return [
		{
			"label": _("Haneen"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "School",
					"description": _("School"),
				},
				
			]
		}
]
