from unittest import mock

from django.contrib.auth import get_user_model
from django.test import TestCase


class TestViews(TestCase):
    def setUp(self):
        """
        functiion that runs before test starts
        """

        User = get_user_model()
        self.user = User.objects.create_user(
            "temporary", "temporary@gmail.com", "temporary"
        )

    def test_user_profile(self):
        self.client.login(username="temporary", password="temporary")
        response = self.client.get("/accounts/profile/")
        self.assertEqual(response.status_code, 200)

        data = {
            "full_name": "test name",
            "phone_number": "01230123",
            "postcode": "235",
            "town_city": "tets",
            "street_address1": "adres",
            "street_address2": "adres2",
            "county": "dub",
        }
        response = self.client.post("/accounts/profile/", data)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self.client.login(username="temporary", password="temporary")
        self.assertIn("_auth_user_id", self.client.session)
        response = self.client.get("/accounts/logout/")
        self.assertEqual(response.status_code, 302)
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_registration(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.client.login(username="temporary", password="temporary")
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 302)

    def test_contact(self):
        page = self.client.get("/accounts/contact/")
        self.assertEqual(page.status_code, 200)
        with mock.patch("accounts.mails.send_mail"):
            page = self.client.post(
                "/accounts/contact/",
                {"email": "test@test.com", "message": "test", "name": "test"},
            )
        self.assertEqual(page.status_code, 200)

    def test_about(self):
        page = self.client.get("/accounts/about/")
        self.assertEqual(page.status_code, 200)

    def test_return_policy(self):
        page = self.client.get("/accounts/return-policy/")
        self.assertEqual(page.status_code, 200)

    def test_delivery(self):
        page = self.client.get("/accounts/delivery/")
        self.assertEqual(page.status_code, 200)

    def test_subscribe(self):
        page = self.client.get("/accounts/test@test.com/subscribe/")
        self.assertEqual(page.status_code, 302)

    def test_login(self):
        page = self.client.post(
            "/accounts/login/", {"username": "invalid", "passsword": "invalid"}
        )
        self.assertNotIn("_auth_user_id", self.client.session)
        self.assertEqual(page.status_code, 200)
        data = {"username": self.user.username, "password": "temporary"}
        page = self.client.post("/accounts/login/", data)
        self.assertEqual(page.status_code, 302)
        page = self.client.post("/accounts/login/", data)
        self.assertEqual(page.status_code, 302)
        with mock.patch("accounts.views.auth.authenticate"):
            response = self.client.post("/accounts/login/", data=data)
            self.assertEqual(response.status_code, 302)
        page = self.client.get("/accounts/login/", data)
        self.assertEqual(page.status_code, 302)


class RegisterTestCases(TestCase):
    def test_registration_post(self):
        data = {
            "email": "test@test.com",
            "username": "test_user",
            "password1": "test_password1",
            "password2": "test_password1",
        }
        response = self.client.post("/accounts/register/", data=data)
        self.assertEqual(response.status_code, 302)
        User = get_user_model()
        user = User.objects.get(email="test@test.com")
        self.assertIsNotNone(user)
        with mock.patch("accounts.views.auth.authenticate"):
            response = self.client.post("/accounts/register/", data=data)
            self.assertEqual(response.status_code, 302)
