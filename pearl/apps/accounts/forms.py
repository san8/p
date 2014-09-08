from django import forms                                

from captcha.fields import CaptchaField                                
from passwords.fields import PasswordField                                
from registration.forms import RegistrationForm

from .models import Customer 
                                

class CustomerForm(RegistrationForm):
    name = forms.CharField(max_length=50, required=False)
    company = forms.CharField(max_length=50, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    captcha = CaptchaField()


class SignUpForm(forms.Form):                                
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    email_id = forms.EmailField(required=False)
    password = PasswordField(required=False)
    company = forms.CharField(label='Company/Website',
            max_length=50, required=False)
    phone_no = forms.CharField(max_length=15, required=False) 
    captcha = CaptchaField(label='Are you human?', required=False)
    terms_and_conditions = forms.CharField(
            label='', widget=forms.CheckboxInput,
            help_text='I agree to Pearl terms and conditions.')             
                                                   

class EditProfileForm():
    class Meta:
        model = Customer 
        fields = ['company',]

