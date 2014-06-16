from django import forms
from passwords.fields import PasswordField


"""
class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    company = forms.CharField(max_length = 100)
    email_id = forms.EmailField()
    password = PasswordField()
    phone_no = forms.CharField(max_length = 15) 
    website = forms.URLField(required = False)
    terms_and_conditions = forms.CharField(widget = forms.CheckboxInput)


    Captcha

"""
class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    def save(self, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
