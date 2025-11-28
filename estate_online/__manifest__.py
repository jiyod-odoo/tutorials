# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'estate_online',
    'depends': ['base', 'base_import_module'],
    'license': 'AGPL-3',
    'author': 'JIYOD',
    "category": 'Real Estate/Brokerage',
    'data': [
        # Model
        'models/estate_online.xml',
        # Security
        'security/ir.model.access.csv',
        # Views
        'views/estate_online_views.xml',
        'views/estate_menus.xml',
        # Actions
    ],
}
