from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    congratulatory_text = fields.Char("Congrat", default="Congratulation Customer!!", store=False)
