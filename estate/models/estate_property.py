from odoo import fields, models, api

from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"
    
    def _next_three_month(self):
        return fields.Date.today() + relativedelta(months=3)
    
    # Core Fields
    name = fields.Char('Title',required=True)
    postcode = fields.Char()
    bedrooms = fields.Integer('Bedrooms',default=2)
    living_area = fields.Float('Living Area (sqm)')
    expected_price = fields.Float('Expected Price',required=True)
    selling_price = fields.Float('Selling Price',readonly=True, copy=False)
    available_from = fields.Date('Available From',copy=False, default=_next_three_month)
    description = fields.Char()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garage_area = fields.Float()
    garden_orientation = fields.Char()
    total_area = fields.Float('Total Area (sqm)',compute="_compute_total_area")
    active = fields.Boolean('Active', default=True,)
    state = fields.Selection([
        ('new','New'),        
        ('offer received','Offer Received'),
        ('offer accepted', 'Offer Accepted'),
        ('sold','Sold'),
        ('cancelled', 'Cancelled'),
    ], default='new', required=True, copy=False)


    # Relational 
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    seller_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", inverse_name="property_id", string="Offers")
    
    @api.depends("living_area","garage_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garage_area

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden: 
            self.garage_area = 10
            self.garden_orientation = "North"
        else:
            self.garage_area = 0
            self.garden_orientation = ""