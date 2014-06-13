from django import forms


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    company = forms.CharField(max_length = 100)
    password = forms.PasswordInput()
    email_id = forms.EmailField()
    agreement = forms.CheckboxInput()


"""
    Captcha

"""
