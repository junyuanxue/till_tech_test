class Payment(object):

    def __init__(self, order):
        self._order = order
        self._paid_amount = 0

    def pay(self, amount):
        self._paid_amount = amount

    def show_paid_amount(self):
        return self._paid_amount

    def calculate_change(self):
        total = self._order.total()
        return round(self._paid_amount - total, 2)
