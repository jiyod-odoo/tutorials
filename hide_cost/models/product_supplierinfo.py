from odoo import models, fields


class ProductSupplierInfo(models.Model):
    # Inheritance
    _inherit = "product.supplierinfo"

    price = fields.Float(
        'Unit Price', digits='Product Price', default=0.0, help="The price to purchase a product", groups="hide_cost.show_product_cost_user")
