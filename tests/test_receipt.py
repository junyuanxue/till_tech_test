import unittest
import json
from unittest.mock import MagicMock
from app.receipt import Receipt

class ReceiptTestCase(unittest.TestCase):

    def setUp(self):
        menu = { "Latte": 4.75, "Capuccino": 3.85 }
        self.order = MagicMock()
        self.payment = MagicMock()
        self.receipt = Receipt(self.order, menu, self.payment)

    def test_output_as_json(self):
        self.order.show_items = MagicMock(return_value = { "Latte": 1, "Capuccino": 2 })
        self.order.calculate_tax = MagicMock(return_value = 1.08)
        self.order.total = MagicMock(return_value = 12.45)
        self.payment.show_paid_amount = MagicMock(return_value = 15)
        self.payment.calculate_change = MagicMock(return_value = 2.55)
        expected_output = {
            "Latte": "1 x $4.75",
            "Capuccino": "2 x $3.85",
            "Tax": "$1.08",
            "Total": "$12.45",
            "Cash": "$15.00",
            "Change": "$2.55"
        }
        self.assertEqual(self.receipt.output_as_json(), json.dumps(expected_output))
