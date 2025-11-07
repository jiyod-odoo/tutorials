import logging

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare

_logger = logging.getLogger(__name__)  # for debugging purpose


class SaleBranch(models.Model):
    _name = "sale.branch"
    _description = "Sale Branch"

    # Core
    name = fields.Char("Name", required=True)
    code = fields.Char("Code")
    sequence = fields.Char("Sequence") # To be delete -> replace by sequence_id instead

    # Relational
    sequence_id = fields.Many2one("ir.sequence", "Sequence")

    # ----------------------------- CRUD Method ----------------------------- #
    @api.model
    def create(self, vals):
        SaleBranch = super().create(vals)
        Sequence = self.env['ir.sequence'].create({
            "name": f"sale.branch.sequence.{SaleBranch.code}",
            "code": f"sale.branch.sequence.{SaleBranch.code}",
            "prefix": SaleBranch.code,
            "padding": 5,
        })
        SaleBranch.write({'sequence_id': Sequence.id})
        return SaleBranch
