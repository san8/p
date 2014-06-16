from django.db import models

# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100)
    email_id = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 100)
    phone_no = models.CharField(max_length = 100)
    website = models.URLField(max_length = 100)

"""
# adding more fields to the django-allauth
from django.contrib.auth.models import AbstractUser

 
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(choices=genders, 
                               default=genders.female, 
                               max_length=20, blank=True)
    REQUIRED_FIELDS = ["email"]


"""

