'''
from django.test import TestCase 
from mock import Mock 

from ..midddlewares import TimezoneMiddleware


class TimezoneMiddlewareTestCase(TestCase):

    def setUp(self):
        self.tm = TimezoneMiddleware()
        self.request = Mock()
        self.request.session = {}

    def test_process_request_without_timezone(self):
        self.assertEqual(self.tm.process_request(self.request), None)

    def test_process_request_with_timezone(self):
        data = { 'django_timezone': 'Asia/Kolkata' }
        self.request.session = {data}
        self.assertEqual(self.tm.process_request(self.request), None)

'''



