from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError
from dateutil.relativedelta import relativedelta
from odoo.tools import float_compare
import logging

_logger = logging.getLogger(__name__)  # for debugging purpose


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"
    _order = "price desc"

    # Core
    price = fields.Float()
    status = fields.Selection([
        ('refused', 'Refused'),
        ('accepted', 'Accepted'),
    ], copy=False)

    # Relational
    partner_id = fields.Many2one(
        "res.partner", required=True, string="Partner")
    property_id = fields.Many2one(
        "estate.property", required=True, string="Property", store=True)
    property_type_id = fields.Many2one(
        "estate.property.type", related='property_id.property_type_id', store=True)

    # Compute
    validity = fields.Integer("Validity (days)", default=7)
    date_deadline = fields.Date(
        "Deadline", compute="_compute_deadline", inverse="_validity_inverse", store=True)

    # -------------------------- Compute Method -------------------------- #
    @api.depends("create_date", "validity")
    def _compute_deadline(self):
        for record in self:
            create_date = record.create_date if record.create_date else fields.Date.today()
            record.date_deadline = create_date + \
                relativedelta(days=record.validity)

    def _validity_inverse(self):
        for record in self:
            # _logger.info("valid inverse")
            create_date = record.create_date if record.create_date else fields.Date.today()
            record.validity = (record.date_deadline - create_date.date()).days

    # -------------------------- Action -------------------------- #
    def handle_accepted(self):
        if "accepted" in self.mapped("property_id.offer_ids.status"):
            raise UserError("Offer already accepted")
        self.status = "accepted"
        self.property_id.selling_price = self.price
        self.property_id.buyer_id = self.partner_id
        self.property_id.state = "offer accepted"
        return True

    def handle_refused(self):
        self.status = "refused"
        return True

    # -------------------------- Override CRUD Method -------------------------- #
    @api.model
    def create(self, vals):
        # vals is list
        for record in vals:
            if record['property_id'] and record['price']:
                property = self.env['estate.property'].browse(
                    record['property_id'])
                _logger.info(property)
                if property.offer_ids:
                    max_offer = max(property.mapped("offer_ids.price"))
                    if float_compare(record['price'], max_offer, 2) <= 0:
                        raise ValidationError(
                            "New offer must higher than an existing offer.")
                    property.state = "offer received"
        return super().create(vals)
