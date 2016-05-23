class Order(object):

    def __init__(self, menu):
        self._items = {}
        self._menu = menu
        self._prices = []
        self._DEFAULT_TAX_RATE = 0.0864
        self._DEFAULT_DISCOUNT_THRESHOLD = 50
        self.DEFAULT_DISCOUNT = 0.05
        self.DEFAULT_MUFFIN_DISCOUNT = 0.1

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
        if self._is_large_purchase():
            return total * (1 - self.DEFAULT_DISCOUNT)
        else:
            return total

    def _sum_items(self):
        self._calcaulate_each_item()
        return round(sum(self._prices), 2)

    def _calcaulate_each_item(self):
        for item, quantity in self._items.items():
            price = self._menu[item] * quantity
            if self._has_muffin(item):
                discounted_price = price * (1 - self.DEFAULT_MUFFIN_DISCOUNT)
                self._prices.append(round(discounted_price, 2))
            else:
                self._prices.append(price)

    def _is_large_purchase(self):
        return self._sum_items() > self._DEFAULT_DISCOUNT_THRESHOLD

    def _has_muffin(self, item):
        return "muffin" in item.lower()
