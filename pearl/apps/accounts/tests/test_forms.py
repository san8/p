# -*- coding: utf-8 -*-
from __future__ import absolute_import

# third party stuff
from django.test import TestCase

# pearl stuff
from ..forms import SignupForm


class SignupFormTest(TestCase):

    def setUp(self):
        self.salutation = 'Mr.'
        self.first_name = 'test'
        pass

    def test_init(self):
        # SignupForm(salutation=self.salutation)
        SignupForm()

    def test_blank_data(self):
        form = SignupForm()
        self.assertFalse(form.is_valid())

    def test_valid_data(self):
        form_data = {'first_name': 'first',
                     'last_name': 'last test',
                     'phone_number': '239384',
                     'email': 'test@test.com',
                     'password1': '123123',
                     'password2': '123123'}
        form = SignupForm(data=form_data)
        self.assertEqual(form.is_valid(), True)
