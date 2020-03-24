from django.test import TestCase
from .models import Product


class ProductTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(test_name.name, 'A product')

    def test_list_products(self):
        pdt = Product(name='A product', description='test', price= '10')
        pdt.description
        response= self.client.get('/')
        self.assertEqual(pdt.description, 'test')



