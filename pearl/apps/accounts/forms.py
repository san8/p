# -*- coding: utf-8 -*-
from __future__ import absolute_import

# third party packages
from django import forms
from nocaptcha_recaptcha.fields import NoReCaptchaField

# pearl stuff
from apps.base.constants import SALUTATION_LIST


class SignupForm(forms.Form):
    """
    User signup form.
    """

    salutation = forms.ChoiceField(choices=SALUTATION_LIST,)
    first_name = forms.CharField(max_length=30, label='First Name',
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='Last Name',
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'Last Name'}))
    phone_number = forms.CharField(max_length=20,
                                   widget=forms.TextInput(
                                       attrs={'placeholder': 'Phone Number'}))
    institution = forms.CharField(max_length=100,
                                  widget=forms.TextInput(
                                      attrs={'placeholder': 'Institution'}))
    captcha = NoReCaptchaField(gtag_attrs={'data-theme': 'light'})

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        captcha_field = self.fields.pop('captcha')
        self.fields['captcha'] = captcha_field
