class OrderProcessor:

    def process_order(self, order):
        total_price = 0
        discount = 0
        shipping_cost = 0
        tax = 0

        if order is None:
            return "error"

        if "items" not in order:
            return "error"

        for item in order["items"]:
            if item["type"] == "book":
                total_price += item["price"] * item["quantity"]
            elif item["type"] == "food":
                total_price += item["price"] * item["quantity"]
            elif item["type"] == "electronics":
                total_price += item["price"] * item["quantity"]
            else:
                total_price += item["price"] * item["quantity"]

        if order["customer_type"] == "regular":
            discount = total_price * 0.05
        elif order["customer_type"] == "vip":
            discount = total_price * 0.1
        elif order["customer_type"] == "employee":
            discount = total_price * 0.2
        else:
            discount = 0

        if order["delivery"] == "standard":
            shipping_cost = 10
        elif order["delivery"] == "express":
            shipping_cost = 25
        elif order["delivery"] == "pickup":
            shipping_cost = 0
        else:
            shipping_cost = 10

        if order["country"] == "US":
            tax = total_price * 0.07
        elif order["country"] == "DE":
            tax = total_price * 0.19
        elif order["country"] == "UK":
            tax = total_price * 0.2
        else:
            tax = total_price * 0.15

        final_price = total_price - discount + shipping_cost + tax

        if final_price < 0:
            final_price = 0

        result = {
            "total": total_price,
            "discount": discount,
            "shipping": shipping_cost,
            "tax": tax,
            "final": final_price
        }

        return result
