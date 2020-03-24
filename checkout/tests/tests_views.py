from django.test import TestCase


    def test_checkout(self):
        page= self.client.get("/checkout")
        self.assertEqual(page.status_code, 200)

    def test_shipping(self):
        page= self.client.get("/checkout/shipping")
        self.assertEqual(page.status_code, 200)

    def test_order_history(self):
        page= self.client.get("/checkout/order_history")
        self.assertEqual(page.status_code, 200)

    