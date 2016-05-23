import json

class Receipt(object):

    def __init__(self, order, menu, payment):
        self._order = order
        self._menu = menu
        self._payment = payment

    def output_as_json(self):
        receipt = {}
        for item in self._order.show_items():
            if self._has_muffin(item):
                discount = self._order.DEFAULT_MUFFIN_DISCOUNT
                receipt[item] = self._format_muffin_discount(discount, item)
            else:
                receipt[item] = self._format_line(item)
        if self._order.is_large_purchase():
            discount = self._order.DEFAULT_DISCOUNT
            items_sum = self._order.show_sum()
            receipt["Disc"] = self._format_order_discount(discount, items_sum)
        receipt["Tax"] = self._format_currency(self._order.calculate_tax())
        receipt["Total"] = self._format_currency(self._order.total())
        receipt["Cash"] = self._format_currency(self._payment.show_paid_amount())
        receipt["Change"] = self._format_currency(self._payment.calculate_change())
        return json.dumps(receipt)

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
