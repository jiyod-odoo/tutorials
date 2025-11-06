from odoo import models, fields

class ResUsers(models.Model):
    # Meta-data
    _inherit = "res.users"
    
    # Core
    # Add Domain to filter only available property
    property_ids = fields.One2many("estate.property", inverse_name="seller_id", string="Properties")
    