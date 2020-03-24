from django.test import TestCase

    def test_view_cart(self):
        page = self.client.get("/cart/view_cart")
        self.assertEqual(page.status_code, 200)

    def test_add_to_cart(self):
        page = self.client.get("/cart/add_to_cart")
        self.assertEqual(page.status_code, 200)

    def test_adjust_cart(self):
        page = self.client.get("/cart/adjust_cart")
        self.assertEqual(page.status_code, 200)

    

