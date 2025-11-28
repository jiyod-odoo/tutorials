{
    'name': '[Sahakim Motor] Hide cost from users',
    'version': '1.0',
    'author': 'odoo JIYOD',
    'category': 'Show Product Cost',
    'depends': [
        'sale_margin'
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        'security/security.xml',
        # View
        'views/product_product_views.xml',
        'views/product_template_views.xml',
        'views/product_supplierinfo_views.xml',
        'views/sale_order_line_views.xml',

    ],
    'license': 'LGPL-3',
    'task': '[#5264269]'
}
