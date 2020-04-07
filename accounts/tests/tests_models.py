from accounts.models import Customer
from django.contrib.auth import get_user_model
from django.test import TestCase


class TestModels(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            "temporary", "temporary@gmail.com", "temporary"
        )
        self.customer = Customer.objects.create(user=self.user)

    def test_customer_name(self):
        self.assertEqual(str(self.customer), self.customer.user.email)
