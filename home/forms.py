from django import forms
from django.forms.extras.widgets import SelectDateWidget
from passwords.fields import PasswordField


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    company = forms.CharField(max_length = 100)
    email_id = forms.EmailField()
    password = PasswordField()
    phone_no = forms.CharField(max_length = 15) 
    website = forms.URLField(required = False)
    terms_and_conditions = forms.CharField(widget = forms.CheckboxInput)


"""
    Captcha

"""
