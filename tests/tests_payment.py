import unittest
from unittest.mock import MagicMock
from app.payment import Payment

class PaymentTestCase(unittest.TestCase):

    def setUp(self):
        self.order = MagicMock()
        self.payment = Payment(self.order)
        self.payment.pay(15)

    def test_pay_and_show_paid_amount(self):
        self.assertEqual(self.payment.show_paid_amount(), 15)

    def test_calculate_change(self):
        self.order.total = MagicMock(return_value = 12.45)
        self.assertEqual(self.payment.calculate_change(), 2.55)
