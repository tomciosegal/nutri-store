from django.test import TestCase


class TestViews(TestCase):
    def test_products_page(self):
        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)

    def test_str(self):
        test_name = Product(name="A product")
        self.assertEqual(test_name.name, "A product")

    def test_list_products(self):
        Product(name="A product", description="test", price="10")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
