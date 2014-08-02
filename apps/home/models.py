"""
from django.db import models

from django.contrib.auth.models import User 


class Customers(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100)
    email_id = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 100)
    phone_no = models.CharField(max_length = 100)
    website = models.URLField(max_length = 100)
    new_field = models.CharField(max_length = 100)


class Profile(models.Model):
    customer = models.ForeignKey(User, related_name='customer id')
    time_zone = models.CharField(max_length=50, blank=True)


# adding more fields to the django-allauth
from django.contrib.auth.models import AbstractUser

 
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(choices=genders, 
                               default=genders.female, 
                               max_length=20, blank=True)
    REQUIRED_FIELDS = ["email"]


"""

