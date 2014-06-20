from django.db import models
from django.contrib.auth.models import User, UserManager

class CustomUser(User):
    company = models.CharField(max_length=100)

    objects = UserManager()
