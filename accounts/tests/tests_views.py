from django.contrib.auth import get_user_model
from django.test import TestCase


class TestViews(TestCase):
    def setUp(self):
        """
        functiion that runs before test starts
        """

        User = get_user_model()
        User.objects.create_user(
            "temporary", "temporary@gmail.com", "temporary"
        )

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)

    def test_user_profile(self):
        self.client.login(username="temporary", password="temporary")
        response = self.client.get("/accounts/profile/")
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
