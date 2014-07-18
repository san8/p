from django.test import TestCase
from django.core.urlresolvers import reverse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 


class ProjectViewsTestCase(TestCase):
    def test_dashboard(self):
        response = self.client.get(reverse('project:project_dashboard'))
        self.assertEqual(response.status_code, 302)
        self.user = User.objects.create(username='testuser', password='12345',
                is_active=True, is_staff=True, is_superuser=True) 
        self.user.set_password('hello') 
        self.user.save() 
        self.user = authenticate(username='testuser', password='hello') 
        login = self.client.login(username='testuser', password='hello') 
        self.assertTrue(login)
        response = self.client.get(reverse('project:project_dashboard'))
        self.assertEqual(response.status_code, 200)
