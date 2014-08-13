"""
Tests for functions.
"""

from model_mommy import mommy

from django.test import TestCase

from ..functions import do_qc

from apps.project.models import NewProject


class FunctionsTestCase(TestCase):

    def test_do_qc(self):
        n = mommy.make('NewProject', file_type='fastq')
        result = do_qc(n.id)
        assertTrue(result)
