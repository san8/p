from django import forms                                
from passwords.fields import PasswordField                                
from captcha.fields import CaptchaField                                
from .models import Customer 
                                
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
                                                   
class CustomersForm():
    pass



class EditProfileForm():
    class Meta:
        model = Customer 
        fields = ['company',]



"""
class UserForm(forms.ModelForm):
    password =  forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', )


"""
