""" 
from django.contrib.auth.models import User

from celery import task 

from .models import UserProfile 


@task
def create_user(data):
    user = User.objects.create_user(
    username = data['username'], email=None, password=data['password'],)
    user.save()
    profile = UserProfile()
    profile.user = user
    profile.token = generate_token()
    profile.save()
    return None 
""" 
