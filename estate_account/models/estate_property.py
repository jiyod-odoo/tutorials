from odoo import models


class EstateProperty(models.Model):
    # Inheritance
    _inherit = "estate.property"

    def handle_sold(self):
        # Check write access
        self.check_access('write')
        # Create Invoice when Property Sold
        self.env["account.move"].sudo().create({
            "partner_id": self.buyer_id.id,
            "move_type": "out_invoice",
            "invoice_line_ids": [
                (0, 0, {
                    'name': self.name,
                    'quantity': 1,
                    'price_unit': self.selling_price * 1.06,
                }),
                (0, 0, {
                    'name': "Admin Fees",
                    'quantity': 1,
                    'price_unit': 100,
                })
            ]
        })
        return super().handle_sold()
