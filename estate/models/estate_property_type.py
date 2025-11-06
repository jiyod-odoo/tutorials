from odoo import _, fields, models

class EstatePropertyType(models.Model):
    # Meta-data
    _name = "estate.property.type"
    _description = "Estate Property Type"
    _order = "sequence,name"
    # SQL Constraint
    _unique_type = models.Constraint(
        "unique (name)",
        "Type name must be unique"
    )    
    # Core
    name = fields.Char(required=True)
    property_ids = fields.One2many("estate.property", inverse_name="property_type_id", string="Properties")
    sequence = fields.Integer('Sequence', default=1)
    offer_count = fields.Integer(compute="_compute_offer_count")
    offer_ids = fields.One2many("estate.property.offer", inverse_name="property_type_id", string="Offers")
    
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)