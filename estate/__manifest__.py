# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'estate',
    'depends': ['base'],
    'license': 'AGPL-3',
    'author': 'JIYOD',
    'data': [
        # Security
        'security/ir.model.access.csv',
        # Views
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_views.xml',
        # Menus
        'views/estate_menus.xml',
        
    ]
   
}