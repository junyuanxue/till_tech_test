import unittest
import json
from unittest.mock import MagicMock
from app.receipt import Receipt

class ReceiptTestCase(unittest.TestCase):

    def setUp(self):
        menu = { "Latte": 4.75, "Blueberry Muffin": 4.05 }
        self.order = MagicMock()
        self.payment = MagicMock()
        self.receipt = Receipt(self.order, menu, self.payment)

    def test_output_as_json(self):
        self.order.show_items.return_value = { "Latte": 10, "Blueberry Muffin": 1 }
        self.order.is_large_purchase.return_value = True
        self.order.DEFAULT_DISCOUNT = 0.05
        self.order.calculate_tax.return_value = 4.38
        self.order.show_sum.return_value = 50.7
        self.order.total.return_value = 48.17
        self.payment.show_paid_amount.return_value = 50
        self.payment.calculate_change.return_value = 1.83
        expected_output = {
            "Latte": "10 x $4.75",
            "Blueberry Muffin": "1 x $4.05 10% off",
            "Disc": "5% from $50.70",
            "Tax": "$4.38",
            "Total": "$48.17",
            "Cash": "$50.00",
            "Change": "$1.83"
        }
        self.assertEqual(self.receipt.output_as_json(), json.dumps(expected_output))
