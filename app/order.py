class Order(object):

    def __init__(self, menu):
        self._items = {}
        self._menu = menu
        self._prices = []
        self._DEFAULT_TAX_RATE = 0.0864
        self._DEFAULT_DISCOUNT_THRESHOLD = 50
        self._DEFAULT_DISCOUNT = 0.05
        self._DEFAULT_MUFFIN_DISCOUNT = 0.1

    def show_items(self):
        return self._items

    def add_item(self, item, quantity = 1):
        if item in self._items:
            self._items[item] += quantity
        else:
            self._items[item] = quantity

    def calculate_tax(self):
        tax = self._sum_items() * self._DEFAULT_TAX_RATE
        return round(tax, 2)

    def total(self):
        total = self._sum_items()
        if self._is_large_purchase(total):
            return total * (1 - self._DEFAULT_DISCOUNT)
        else:
            return total

    def _sum_items(self):
        self._calcaulate_each_item()
        return round(sum(self._prices), 2)

    def _calcaulate_each_item(self):
        for item, quantity in self._items.items():
            self._prices.append(self._menu[item] * quantity)

    def _is_large_purchase(self, amount):
        return amount > self._DEFAULT_DISCOUNT_THRESHOLD
