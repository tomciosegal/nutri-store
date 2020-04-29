from unittest import mock

from django.test import TestCase
from products.models import Product


class TestViews(TestCase):
    def test_products_page(self):
        page = self.client.get("/products/")
        self.assertEqual(page.status_code, 200)
        page = self.client.get("/products/?page=test")
        self.assertEqual(page.status_code, 200)
        page = self.client.get("/products/?page=100")
        self.assertEqual(page.status_code, 200)
        page = self.client.get("/products/?q=test")
        self.assertEqual(page.status_code, 200)
        page = self.client.get("/products/?category_id=1")
        self.assertEqual(page.status_code, 200)

    def test_str(self):
        test_name = Product(name="A product")
        self.assertEqual(test_name.name, "A product")

    def test_product_detail(self):
        product = Product.objects.create(
            name="A product", description="test", price="10", quantity=10
        )
        response = self.client.get(f"/products/product_details/{product.id}")
        self.assertEqual(response.status_code, 200)

    def test_products_page_post(self):
        with mock.patch("products.views.send_subscribe_mail"):
            page = self.client.post("/products/")
        self.assertEqual(page.status_code, 200)
