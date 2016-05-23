class Payment(object):

    def __init__(self, order):
        self._order = order
        self._paid_amount = 0

    def pay(self, amount):
        self._paid_amount = amount

    def show_paid_amount(self):
        return self._paid_amount

    def calculate_change(self, amount):
        total = self._order.total()
        return round(amount - total, 2)
