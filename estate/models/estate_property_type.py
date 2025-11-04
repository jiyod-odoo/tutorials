from odoo import fields, models, api

from datetime import date
from dateutil.relativedelta import relativedelta

def three_months_from_today():
    return date.today() + relativedelta(months=3)

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"
    
    name = fields.Char('Title',required=True)
    postcode = fields.Char()
    bedrooms = fields.Integer('Bedrooms',default=2)
    living_area = fields.Float('Living Area (sqm)')
    expected_price = fields.Float('Expected Price',required=True)
    selling_price = fields.Float('Selling Price',readonly=True, copy=False)
    available_from = fields.Date('Available From',copy=False, default=fields.Date.today)
    description = fields.Char()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garage_area = fields.Float()
    garden_orientation = fields.Char()
    active = fields.Boolean('Active', default=True)
    state = fields.Selection([
        ('new','New'),        
        ('offer received','Offer Received'),
        ('offer accepted', 'Offer Accepted'),
        ('sold','Sold'),
        ('cancelled', 'Cancelled'),
    ], default='new', required=True, copy=False)
    