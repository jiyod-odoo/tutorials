from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero
from dateutil.relativedelta import relativedelta


class EstateProperty(models.Model):
    # Meta-data
    _name = "estate.property"
    _description = "Estate Property"
    _order = "id desc"
    # SQL Constraint
    _check_expected_price = models.Constraint(
        'CHECK (expected_price > 0)',
        'Expected Price must be positive'
    )
    _check_selling_price = models.Constraint(
        'CHECK (0 <= selling_price)',
        'Selling Price must be positive'
    )
    _check_best_offer = models.Constraint(
        'CHECK (0 <= best_offer)',
        'Best Offer Price must be positive'
    )

    # -------------------------- Default Method -------------------------- #
    def _next_three_month(self):
        return fields.Date.today() + relativedelta(months=3)

    # Core Fields
    name = fields.Char('Title', required=True)
    postcode = fields.Char()
    bedrooms = fields.Integer('Bedrooms', default=2)
    living_area = fields.Float('Living Area (sqm)')
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price', readonly=True, copy=False)
    available_from = fields.Date(
        'Available From', copy=False, default=_next_three_month)
    description = fields.Char()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Float()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ], default='north')
    active = fields.Boolean('Active', default=True,)
    state = fields.Selection([
        ('new', 'New'),
        ('offer received', 'Offer Received'),
        ('offer accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled'),
    ], default='new', required=True, copy=False, string='Status')

    # Relational
    property_type_id = fields.Many2one(
        "estate.property.type", string="Property Type")
    seller_id = fields.Many2one(
        "res.users", string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many(
        "estate.property.offer", inverse_name="property_id", string="Offers")

    # Compute
    best_offer = fields.Float(
        'Best Offer', compute="_compute_best_offer", store=True)
    total_area = fields.Float(
        'Total Area (sqm)', compute="_compute_total_area")

    # -------------------------- Compute Method -------------------------- #
    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_offer(self):
        for record in self:
            prices = record.offer_ids.mapped('price')
            record.best_offer = max(prices) if prices else 0

    # --------------------------  Constraint & On Change -------------------------- #
    @api.constrains('selling_price')
    def _check_selling_price_above(self):
        for record in self:
            if not float_is_zero(record.expected_price, 2) and float_compare(record.selling_price, record.expected_price * 0.90, precision_digits=2) <= 0:
                raise ValidationError(
                    "Selling Price must more than 90 percent Expected Price")

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = ""

    # -------------------------- Override CRUD Method -------------------------- #

    @api.ondelete(at_uninstall=False)
    def _unlink_except_new_or_cancelled(self):
        for record in self:
            if record.state not in ('new', 'cancelled'):
                raise UserError(
                    "Can't delete properties that already have offer!")

    # -------------------------- Action -------------------------- #
    def handle_sold(self):
        if self.state == "cancelled":
            raise UserError("cancel property cannot be sold")
        else:
            self.state = "sold"
        return True

    def handle_cancel(self):
        if self.state == "sold":
            raise UserError("sold property cannot be sold")
        else:
            self.state = "cancelled"
        return True
