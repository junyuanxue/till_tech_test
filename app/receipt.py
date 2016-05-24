import json

class Receipt(object):

    def __init__(self, order, menu, payment):
        self._order = order
        self._menu = menu
        self._payment = payment
        self._body = {}

    def output_as_json(self):
        self._print_items()
        if self._order.is_large_purchase():
            self._print_discount()
        self._body["Tax"] = self._format_currency(self._order.calculate_tax())
        self._body["Total"] = self._format_currency(self._order.total())
        self._body["Cash"] = self._format_currency(self._payment.show_paid_amount())
        self._body["Change"] = self._format_currency(self._payment.calculate_change())
        return json.dumps(self._body)

    def _print_items(self):
        for item in self._order.show_items():
            if self._has_muffin(item):
                discount = self._order.DEFAULT_MUFFIN_DISCOUNT
                self._body[item] = self._format_muffin_discount(discount, item)
            else:
                self._body[item] = self._format_line(item)

    def _print_discount(self):
        discount = self._order.DEFAULT_DISCOUNT
        items_sum = self._order.show_sum()
        self._body["Disc"] = self._format_order_discount(discount, items_sum)

    def _format_line(self, item):
        quantity = self._order.show_items()[item]
        price = self._format_currency(self._menu[item])
        return "{} x {}".format(quantity, price)

    def _format_order_discount(self, discount, amount):
        formatted_amount = self._format_currency(amount)
        return "{:.0%} from {}".format(discount, formatted_amount)

    def _format_muffin_discount(self, discount, item):
        desc = self._format_line(item)
        return "{} {:.0%} off".format(desc, discount)

    def _format_currency(self, price):
        return "${0:.2f}".format(price)

    def _has_muffin(self, item):
        return "muffin" in item.lower()
