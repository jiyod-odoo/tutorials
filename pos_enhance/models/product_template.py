from odoo import models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def get_product_info_pos(self, price, quantity, pos_config_id, product_variant_id=False):
        # Call the parent class's method to get base info
        product_info = super(ProductTemplate, self).get_product_info_pos(
            price, quantity, pos_config_id, product_variant_id)

        # Update the dictionary using .update() or a new dict merge syntax (Python 3.5+)
        product_info.update({
            'weight': self.weight,
            'volume': self.volume,
        })
        return product_info
