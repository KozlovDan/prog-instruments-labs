class InvalidOrderError(Exception):
    pass


class PricingService:
    def calculate_total(self, items):
        return sum(item["price"] * item["quantity"] for item in items)


class DiscountService:
    DISCOUNTS = {
        "regular": 0.05,
        "vip": 0.10,
        "employee": 0.20
    }

    def calculate(self, total, customer_type):
        return total * self.DISCOUNTS.get(customer_type, 0)


class ShippingService:
    SHIPPING_COSTS = {
        "standard": 10,
        "express": 25,
        "pickup": 0
    }

    def calculate(self, delivery_type):
        return self.SHIPPING_COSTS.get(delivery_type, 10)


class TaxService:
    TAX_RATES = {
        "US": 0.07,
        "DE": 0.19,
        "UK": 0.20
    }

    def calculate(self, total, country):
        return total * self.TAX_RATES.get(country, 0.15)


class OrderProcessor:

    def __init__(self):
        self.pricing = PricingService()
        self.discount = DiscountService()
        self.shipping = ShippingService()
        self.tax = TaxService()

    def process_order(self, order):
        self._validate(order)

        total = self.pricing.calculate_total(order["items"])
        discount = self.discount.calculate(total, order["customer_type"])
        shipping = self.shipping.calculate(order["delivery"])
        tax = self.tax.calculate(total, order["country"])

        final = max(0, total - discount + shipping + tax)

        return {
            "total": total,
            "discount": discount,
            "shipping": shipping,
            "tax": tax,
            "final": final
        }

    def _validate(self, order):
        if not order or "items" not in order:
            raise InvalidOrderError("Invalid order structure")
