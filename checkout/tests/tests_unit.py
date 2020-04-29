from cart.models import Cart, CartItem
from cart.utils import clear_cart, load_cart
from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase
from products.models import Product


class TestViews(TestCase):
    def setUp(self):
        """
        functiion that runs before test starts
        """

        User = get_user_model()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            "temporary", "temporary@gmail.com", "temporary"
        )
        self.cart = Cart.objects.create(user=self.user)
        self.product = Product.objects.create(
            name="test product",
            description="descr test",
            price="10",
            quantity=1,
        )
        self.cart_item = CartItem.objects.create(
            cart=self.cart, product_id=self.product.id, quantity=1
        )

    def test_load_cart(self):
        request = self.factory.get("/")
        request.session = {}
        load_cart(request, self.user)
        self.assertEqual(
            request.session,
            {"cart": {1: 1}, "total": 10.0, "total_after_discount": 10.0},
        )

    def test_clear_cart(self):
        self.assertEqual(Cart.objects.filter(user=self.user).count(), 1)
        self.assertEqual(CartItem.objects.filter(cart=self.cart).count(), 1)

        clear_cart(self.user)

        self.assertEqual(Cart.objects.filter(user=self.user).count(), 0)
        self.assertEqual(CartItem.objects.count(), 0)
