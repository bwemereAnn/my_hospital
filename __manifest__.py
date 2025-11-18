# -*- coding: utf-8 -*-
{
    'name': "my_hospital",

    'summary': "Product for hospitals and patients",

    'description': """
        using this module for complete manage your hospital and get good 
        reports
    """,

    'author': "annette",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/doctors.xml',
        'views/templates.xml',
        'views/appointments.xml',
        'views/menu.xml',
    ],

}
