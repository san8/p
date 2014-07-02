from django.db import models
from django.contrib.auth.models import User

"""
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile')
    token = models.CharField(max_length=32)

"""

class SampleCount(models.Model):
    num = models.IntegerField(default=0)


