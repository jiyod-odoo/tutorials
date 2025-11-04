from odoo import fields, models, api

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"
    
    
    name = fields.Char(required=True)
    expected_price = fields.Float(required=True)
    