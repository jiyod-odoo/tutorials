# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'estate',
    'depends': ['base'],
    'license': 'AGPL-3',
    'author': 'JIYOD',
    # 'version': '19.0.1.0.0', # major.minor.major-module,sub-module,fix-module
    'data': [
        # Security
        'security/ir.model.access.csv',
        # View
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_views.xml',
        'views/res_users_views.xml',
        # Menus
        'views/estate_menus.xml',
        # Report
        'report/estate_property_reports.xml',
        'report/estate_property_templates.xml',
    ],
    'demo': [
        # 'demo/estate_property_type_demo_data.xml'
        # 'demo/estate_property_demo_data.xml'
        'demo/estate_demo_data.xml'
    ],
    'installable': True,
    'application': True,
}
