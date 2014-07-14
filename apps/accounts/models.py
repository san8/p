from django.db import models
from django.contrib.auth.models import User #UserManager

#from captcha.fields import CaptchaField 

class Customer(models.Model):
    user = models.ForeignKey(User, related_name='customer_to_user')
    company = models.CharField(max_length=50, blank=True)
    timezone = models.CharField(max_length=30)

    def __unicode__(self):
        return self.user.username 



""" 
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
