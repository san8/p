from django.db import models
from django.contrib.auth.models import User #UserManager

from captcha.fields import CaptchaField 

class Customer(models.Model):
    user = models.ForeignKey(User, related_name='customer_to_user')
    name = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    captcha = CaptchaField()

    def __unicode__(self):
        return self.user.username 


from registration.signals import user_registered
from .forms import CustomerForm

def user_registered_callback(sender, user, request, **kwargs):
    form =  CustomerForm(request.POST)
    customer = Customer(user=user)
    customer.name = form.data["name"]
    customer.company = form.data["company"]
    customer.phone_number = form.data["phone_number"]
    customer.save()


user_registered.connect(user_registered_callback)

""" 
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

    def __unicode__(self):
        return self.user.username 



class UserForm(ModelForm):
    class Meta:
        model = User  
        fields = ['first_name', 'last_name', 'email', 'password']

    def __unicode__(self):
        return self.name 


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    #picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile 
        fields = ['website', 'captcha']


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']

    def __unicode__(self):
        return self.name 


class CustomUser(User):
    company = models.CharField(max_length=100)

    objects = UserManager()
"""  
