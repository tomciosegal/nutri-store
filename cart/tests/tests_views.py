from cart.models import Cart, CartItem
from django.contrib.auth import get_user_model
from django.test import TestCase
from products.models import Product


class TestViews(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            "temporary", "temporary@gmail.com", "temporary"
        )
        self.cart = Cart.objects.create(user=self.user)
        self.product = Product.objects.create(
            name="test product",
            description="descr test",
            price="10",
            quantity=10,
        )
        self.cart_item = CartItem.objects.create(
            cart=self.cart, product_id=self.product.id, quantity=1
        )

    def test_registration(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)

    def test_view_cart_status_code(self):
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)

    def test_add_to_cart(self):
        page = self.client.get(f"/cart/add/{self.product.id}/")
        self.assertEqual(page.status_code, 302)

    def test_adjust_cart(self):
        page = self.client.get(f"/cart/adjust/{self.product.id}/")
        self.assertEqual(page.status_code, 302)

    def test_adjust_cart_post(self):
        """
        check if cart is adjusted with product
        quantity both in session and Cart Model
        """
        self.client.login(username="temporary", password="temporary")
        session = self.client.session
        session["cart"] = {self.product.id: 7}
        session.save()
        self.client.post(f"/cart/adjust/{self.product.id}/", {"quantity": 3})

        self.assertEqual(
            self.client.session["cart"], {str(self.product.id): 3}
        )
        cart = Cart.objects.filter(user=self.user).first()
        self.assertIsNotNone(cart)
        self.assertEqual(
            CartItem.objects.filter(product_id=self.product.id).count(), 1
        )

        # check if no amend is made when we try to update with to high quantity
        self.client.post(f"/cart/adjust/{self.product.id}/", {"quantity": 12})
        self.assertEqual(
            self.client.session["cart"], {str(self.product.id): 3}
        )
        # check if the is no update when quantity=0
        self.client.post(f"/cart/adjust/{self.product.id}/", {"quantity": 0})
        self.assertEqual(
            self.client.session["cart"], {str(self.product.id): 3}
        )

    def test_cart_item_delete(self):
        self.client.login(username="temporary", password="temporary")
        response = self.client.post(f"/cart/delete/{self.product.id}/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            CartItem.objects.filter(product_id=self.product.id).count(), 0
        )
