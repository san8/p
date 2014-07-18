from django.test import TestCase
from django.core.urlresolvers import reverse 


class AccountsViewsTestCase(TestCase):
    fixtures = ['test_user_login.json']


    def test_register(self):
        response = self.client.get(reverse('registration_register'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('registration_register'))
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get(reverse('auth_login'))
        self.assertEqual(response.status_code, 200)
        login = self.client.login(username='chillaranand', password='123456')
        self.assertTrue(login)
        response = self.client.get(reverse('project:project_dashboard'))
        self.assertEqual(response.status_code, 200)
