from django import forms                                

from captcha.fields import CaptchaField                                
from registration.forms import RegistrationForm

from .models import Customer 
                                

class CustomerForm(RegistrationForm):
    name = forms.CharField(max_length=50, required=False)
    company = forms.CharField(max_length=50, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    captcha = CaptchaField()
