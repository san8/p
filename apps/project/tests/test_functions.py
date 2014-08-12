"""
Tests for functions.
"""
from model_mommy import mommy

from django.test import TestCase

from ..functions import get_files
from ..models import NewProject


        
class FunctionsTestCase(TestCase):

    def test_get_files(self):
        n = mommy.make('NewProject')
        result = get_files(n.id)
        self.assertEqual(result, True)
