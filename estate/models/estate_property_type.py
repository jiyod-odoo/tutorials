from odoo import fields, models

class EstatePropertyType(models.Model):
    # Meta-data
    _name = "estate.property.type"
    _description = "Estate Property Type"
    # SQL Constraint
    _unique_type = models.Constraint(
        'unique (name)',
        'Type name must be unique'
    )    
    # Core
    name = fields.Char(required=True)