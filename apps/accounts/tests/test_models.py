from django.test import TestCase
from django.contrib.auth.models import User 
from captcha.fields import CaptchaField 

from ..models import Customer 


class AccountsModelsTestCase(TestCase):
    def create_Customer(self):
        user = User.objects.all()[0] 
        return Customer.objects.create(user=user, captcha=CaptchaField())

    def test_Customer_creation(self):
        c = self.create_Customer()
        self.assertTrue(isinstance(c, Customer))
        self.assertEqual(c.__unicode__, c.user.name)

