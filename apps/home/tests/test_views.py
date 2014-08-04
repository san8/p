from django.test import TestCase


class HomeViewsTestCase(TestCase):
    def test_home(self):
        resp = self.client.get('/home/')
        self.assertEqual(resp.status_code, 200)

    def test_default(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_faq(self):
        resp = self.client.get('/home/faq/')
        self.assertEqual(resp.status_code, 200)

    def test_unknown_view(self):
        resp = self.client.get('/does-not-exits/')
        self.assertEqual(resp.status_code, 404)
