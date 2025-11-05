from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
import logging

_logger = logging.getLogger(__name__) # for debugging purpose

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"
    
    price = fields.Float()
    status = fields.Selection([
        ('refused','Refused'),
        ('accepted', 'Accepted'),
    ], copy=False)
    partner_id = fields.Many2one("res.partner", required=True, string="Partner")
    property_id = fields.Many2one("estate.property", required=True, string="Property")
    validity = fields.Integer("Validity (days)", default=7)
    date_deadline = fields.Date("Deadline", compute="_compute_deadline", inverse="_validity_inverse", store=True)
    
    @api.depends("create_date", "validity")
    def _compute_deadline(self):
        for record in self:
            create_date = record.create_date if record.create_date else fields.Date.today()
            record.date_deadline = create_date + relativedelta(days=record.validity)

    def _validity_inverse(self):
        for record in self:
            # _logger.info("valid inverse")
            create_date = record.create_date if record.create_date else fields.Date.today()
            record.validity = (record.date_deadline - create_date.date()).days