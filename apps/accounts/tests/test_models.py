from mock import Mock 

from unittest import TestCase 

from ..models import Customer 


class AccountsModelsTestCase(TestCase):
    def create_Customer(self):
        customer = Mock() 
        customer.name = "pearl"
        return customer 

    def test_Customer_creation(self):
        c = self.create_Customer()
        self.assertEqual(c.name, "pearl")
