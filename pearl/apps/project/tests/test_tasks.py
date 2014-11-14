from unittest import TestCase 
from model_mommy import mommy

from django.test.utils import override_settings



class CeleryTasksTestCase(TestCase):

    @override_settings(CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
                       CELERY_ALWAYS_EAGER=True,
                       BROKER_BACKEND='memory')
        
    def test_get_ftp_files(self):
        pass

        
class FunctionsTestCase(TestCase):

    def test_get_files(self):
       pass

    def test_dummy(self):
        pass
        
