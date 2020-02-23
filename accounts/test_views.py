from django.test import TestCase
from django.contrib.auth import get_user_model


class TestViews(TestCase):
    """functiion that runs before test starts"""
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
    
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        

    def test_user_profile(self):
        self.client.login(username= 'temporary', password= 'temporary')
        response= self.client.get("/accounts/profile/")
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self.client.login(username= 'temporary', password= 'temporary')
        self.assertIn('_auth_user_id', self.client.session)
        response= self.client.get("/accounts/logout/")
        self.assertEqual(response.status_code, 302)
        self.assertNotIn('_auth_user_id', self.client.session)
        
    

    
    


    


        
        
        