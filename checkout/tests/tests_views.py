from unittest import mock
from accounts.models import Customer
from django.contrib.auth import get_user_model
from django.test import TestCase
from products.models import Product


class TestView(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            "temporary", "temporary@gmail.com", "temporary"
        )
        Customer.objects.create(user=self.user)

    def test_checkout(self):
        self.client.login(username="temporary", password="temporary")
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)

    def test_shipping(self):
        page = self.client.get("/checkout/shipping/")
        self.assertEqual(page.status_code, 302)

    def test_order_history(self):
        page = self.client.get("/checkout/order_history/")
        self.assertEqual(page.status_code, 200)

    def test_checkout_buying_item(self):

        """
        this test will check if buying product works
        """

        self.client.login(username="temporary", password="temporary")
        product = Product.objects.create(
            name="test product",
            description="descr test",
            price="10",
            quantity=1,
        )
        session = self.client.session
        session["cart"] = {product.id: 7}
        session["total"] = 50
        session.save()
        with mock.patch("stripe.Charge.create") as stripe:
            stripe.return_value.paid = True

            page = self.client.post(
                "/checkout/",
                {
                    "cardholder_name": ["eee"],
                    "stripe_id": ["tok_1GRJXNHnFvIuj2YMwvs3xNEi"],
                },
            )
            self.assertEqual(page.status_code, 302)
            self.assertEqual(self.client.session['cart'], dict())

    def test_order_confirmation(self):
        page = self.client.get("/checkout/order_confirmation/")
        self.assertEqual(page.status_code, 200)
