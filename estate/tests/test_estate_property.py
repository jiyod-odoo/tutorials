from odoo.tests.common import TransactionCase, Form
from odoo.exceptions import UserError
from odoo.tests import tagged
from odoo.fields import Command


@tagged('post_install', '-at_install')
class EstateTestCase(TransactionCase):

    @classmethod
    def setUpClass(cls):
        # add env on cls and many other things
        super().setUpClass()

        # create the data for each tests. By doing it in the setUpClass instead
        # of in a setUp or in each test case, we reduce the testing time and
        # the duplication of code.
        cls.properties = cls.env['estate.property'].create({
            "id": 200,
            "create_date": "2025-11-18 09:30:00",
            "write_date": "2025-11-18 09:30:00",
            "name": "Luxury Downtown Apartment",
            "postcode": "75001",
            "bedrooms": 3,
            "living_area": 120.50,
            "expected_price": 510000.00,
            "selling_price": 500000.00,
            "available_from": "2026-02-18",
            "description": "A spacious and bright apartment with a view of the city center.",
            "facades": 2,
            "garage": True,
            "garden": True,
            "garden_area": 10.00,
            "garden_orientation": "north",
            "active": True,
            "state": "offer received",
            "seller_id": 3,
            "offer_ids": [
                Command.create({
                    "price": 495000.00,
                    "partner_id": 1,
                    "property_id": 200
                }),
                Command.create({
                    "price": 480000.00,
                    "status": "refused",
                    "partner_id": 1,
                    "property_id": 200
                })
            ],
            "best_offer": 495000.00,
            "total_area": 130.50
        })

    def test_creation_area(self):
        """Test that the total_area is computed like it should."""
        self.properties.living_area = 20
        self.assertRecordValues(self.properties, [
            {'name': "Luxury Downtown Apartment", 'total_area': 30},
        ])

    def test_action_sell(self):
        """Test that everything behaves like it should when selling a property."""
        offer = self.env['estate.property.offer'].browse(
            self.properties.offer_ids[0].id)
        offer.handle_accepted()
        self.properties.handle_sold()
        self.assertRecordValues(self.properties, [
            {'name': 'Luxury Downtown Apartment', 'state': 'sold'},
        ])
        with self.assertRaises(UserError):
            self.properties.handle_sold()

    def test_no_new_offer_sold_property(self):
        """ Test no new offer cannot create when property already sold """
        offer = self.env['estate.property.offer'].browse(
            self.properties.offer_ids[0].id)
        offer.handle_accepted()
        self.properties.handle_sold()
        with self.assertRaises(UserError):
            self.env['estate.property.offer'].create(
                {
                    "id": 200,
                    "price": 550000.00,
                    "partner_id": 10,
                    "property_id": self.properties.id,
                })

    def test_form_garden_checkbox(self):
        """ Test form garden UI is hide when uncheck garden """
        context = {
            'name': 'Luxury Downtown Apartment',
            'garden': False,
            'garden_area': 20,
        }
        property_form = Form(self.env['estate.property'].with_context(context))
        property_form.garden = False
        property_form.name = 'Luxury Downtown Apartment'
        self.assertEqual(property_form.garden_area, 0)
        property_form.garden = True
        self.assertEqual(property_form.garden_area, 10)
        self.assertEqual(property_form.garden_orientation, 'north')
