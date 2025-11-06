from odoo import fields, models, Command
import logging

_logger = logging.getLogger(__name__)

class EstateProperty(models.Model):
    # Inheritance
    _inherit = "estate.property"
    
    def handle_sold(self):
        _logger.info("On Sold AES")
        _logger.info(self)
        account_move = self.env["account.move"].create({
            "partner_id": self.buyer_id.id,
            "move_type": "out_invoice",
            "invoice_line_ids": [
                (0, 0,{
                'name': self.name,
                'quantity': 1,
                'price_unit': self.selling_price * 1.06,
                }),
                (0, 0,{
                'name': "Admin Fees",
                'quantity': 1,
                'price_unit': 100,
                })
            ]
        })
        _logger.info(account_move)
        return super().handle_sold()