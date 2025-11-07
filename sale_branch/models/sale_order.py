from odoo import fields, models, api


class SaleOrder(models.Model):
    # Inherit
    _inherit = "sale.order"

    # Relational
    branch_id = fields.Many2one("sale.branch", "Branch")

    # ----------------------------- CRUD Method ----------------------------- #
    @api.model
    def create(self, vals):
        SaleOrder = super().create(vals)
        for record in vals:
            if record['branch_id']:
                new_name = self.env['ir.sequence'].next_by_code(
                    SaleOrder.branch_id.sequence_id.code)
                SaleOrder.write({'name': new_name})
        return SaleOrder
