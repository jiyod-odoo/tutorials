from odoo import models, fields


# Sale Margin
class SaleOrderLine(models.Model):
    # Inheritance
    _inherit = "sale.order.line"

    purchase_price = fields.Float(
        string="Cost", compute="_compute_purchase_price",
        digits='Product Price', store=True, readonly=False, copy=False, precompute=True,
        groups="hide_cost.show_product_cost_user")
