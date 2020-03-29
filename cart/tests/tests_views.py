from django.test import TestCase
from products.models import Product
from django.core.files.uploadedfile import SimpleUploadedFile


class TestViews(TestCase):
    
    def test_registration(self):
        page= self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)

    def test_view_cart_status_code(self):
        product=Product.objects.create(name='test product',description='descr test', price='10', quantity=1  )
        page = self.client.get(f"/cart/view_cart/{product.id}/")
        self.assertEqual(page.status_code, 200)

    def test_add_to_cart(self):
        page = self.client.get("/cart/add/add_to_cart/")
        self.assertEqual(page.status_code, 200)

    def test_adjust_cart(self):
        page = self.client.get("/cart/adjust/adjust_cart/")
        self.assertEqual(page.status_code, 200)

    

