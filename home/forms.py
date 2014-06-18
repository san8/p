from django import forms
from passwords.fields import PasswordField
from allauth.account.forms import SignupForm
from captcha.fields import CaptchaField
#from myapp.forms import widgets


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    company = forms.CharField(max_length = 100)
    email_id = forms.EmailField()
    password = PasswordField()
    phone_no = forms.CharField(max_length = 15) 
    website = forms.URLField(required = False)
    captcha = CaptchaField()
    terms_and_conditions = forms.CharField(widget = forms.CheckboxInput)



"""

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email_id = forms.EmailField()
    phone_no = forms.CharField(max_length = 15) 
    company = forms.CharField(max_length=50)
    password = PasswordField()
    agree = forms.CharField(widget = forms.CheckboxInput, label='I Agree To Pearl Terms & Conditions.')

    def save(self, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email_id = self.cleaned_data['email_id']
        user.phone_no = self.cleaned_data['phone_no']
        user.company = self.cleaned_data['company']
        user.password = self.cleaned_data['password']
        user.save()
"""
class MySignupForm(SignupForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email_id = forms.EmailField()
    phone_no = forms.CharField(max_length = 15) 
    company = forms.CharField(max_length=50)
    password = PasswordField()
    agree = forms.CharField(widget = forms.CheckboxInput, label='I Agree To Pearl Terms & Conditions.')


class SignupFormExtra(forms.Form):
    first_name = forms.CharField(max_length=30, label='asdf')
    last_name = forms.CharField(max_length=30, label='asdfasdf')

    def save(self, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
