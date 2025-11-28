from odoo import models, fields


class ProductProduct(models.Model):
    # Inheritance
    _inherit = "product.product"

    standard_price = fields.Float(
        'Cost', company_dependent=True,
        digits='Product Price',
        groups="hide_cost.show_product_cost_user",
        help="""Value of the product (automatically computed in AVCO).
        Used to value the product when the purchase cost is not known (e.g. inventory adjustment).
        Used to compute margins on sale orders.""")
