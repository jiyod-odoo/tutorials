from odoo import fields, models

class EstatePropertyTag(models.Model):
    # Meta-data
    _name = "estate.property.tag"
    _description = "Estate Property Tag"
    _order = "name"
    # SQL Constraint
    _unique_tag = models.Constraint(
        'unique (name)',
        'Tag name must be unique'
    )
    # Core
    name = fields.Char(required=True)
    color = fields.Integer()
