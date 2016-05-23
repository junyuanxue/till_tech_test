import unittest
from app.order import Order

class OrderTestCase(unittest.TestCase):

    def setUp(self):
        menu = { "Latte": 4.75, "Capuccino": 3.85, "Blueberry Muffin": 4.05 }
        self.order = Order(menu)
        self.order.add_item("Latte")
        self.order.add_item("Capuccino", 2)

    def test_show_items(self):
        self.assertEqual(self.order.show_items(), { "Latte": 1, "Capuccino": 2 })

    def test_calculate_tax(self):
        self.assertEqual(self.order.calculate_tax(), 1.08)

    def test_total(self):
        self.assertEqual(self.order.total(), 12.45)

    def test_calculate_large_purchase_discount(self):
        self.order.add_item("Latte", 9)
        self.assertEqual(self.order.total(), 52.44)

    def test_calculate_muffin_discount(self):
        self.order.add_item("Blueberry Muffin")
        self.assertEqual(self.order.total(), 16.1)
