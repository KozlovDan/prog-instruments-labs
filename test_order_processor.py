import unittest
from code_before import OrderProcessor

class TestOrderProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = OrderProcessor()

    def test_regular_customer_order(self):
        order = {
            "items": [
                {"type": "book", "price": 10, "quantity": 2},
                {"type": "food", "price": 5, "quantity": 4}
            ],
            "customer_type": "regular",
            "delivery": "standard",
            "country": "US"
        }

        result = self.processor.process_order(order)
        self.assertEqual(result["total"], 40)
        self.assertAlmostEqual(result["discount"], 2)
        self.assertAlmostEqual(result["tax"], 2.8)

    def test_vip_customer_order(self):
        order = {
            "items": [
                {"type": "electronics", "price": 100, "quantity": 1}
            ],
            "customer_type": "vip",
            "delivery": "express",
            "country": "DE"
        }

        result = self.processor.process_order(order)
        self.assertEqual(result["total"], 100)
        self.assertEqual(result["shipping"], 25)

    def test_invalid_order(self):
        self.assertEqual(self.processor.process_order(None), "error")

