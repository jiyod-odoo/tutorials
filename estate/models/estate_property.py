from odoo import fields, models, api

from datetime import date
from dateutil.relativedelta import relativedelta

def three_months_from_today():
    return date.today() + relativedelta(months=3)

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"
    
    name = fields.Char(required=True)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    num_bedroom = fields.Integer(default=2)
    available_date = fields.Date(copy=False, default=fields.Date.today)
    active = fields.Boolean('Active', default=True)
    state = fields.Selection([
        ('new','New'),        
        ('offer received','Offer Received'),
        ('offer accepted', 'Offer Accepted'),
        ('sold','Sold'),
        ('cancelled', 'Cancelled'),
    ], default='new', required=True, copy=False)
    