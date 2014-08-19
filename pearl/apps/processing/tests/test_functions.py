"""
Tests for functions.
"""

from model_mommy import mommy

from django.test import TestCase

from ..functions import do_qc


class FunctionsTestCase(TestCase):

    def test_do_qc(self):
        n = mommy.make('NewProject', file_type='fastq', id=999)
        result = do_qc(n.id)
        assertTrue(result)
'''
    def test_unzip_files(self):
        path = os.path.join(MEDIA_ROOT, 'tests')
        result = unzip_files(path)
        assertTrue(result)


    def test_fastq_qc(self):
        path = os.path.join(MEDIA_ROOT, 'tests')
        result = fastq_qc(path)
        assertTrue(result)
'''
        
