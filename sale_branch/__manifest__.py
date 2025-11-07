{
    'name': 'sale_branch',
    'depends': ['sale_management', 'account'],
    'license': 'AGPL-3',
    'author': 'JIYOD',
    'data': [
        # Security
        'security/ir.model.access.csv',
        # View
        'views/sale_branch_views.xml',
        'views/sale_order_views.xml',
        # Menus
        'views/sale_branch_menus.xml',
    ]

}
