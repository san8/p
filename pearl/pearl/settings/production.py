"""Additional settings for Development Environment."""

import os 

from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

#DEBUG = True

#TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pearl',
        'USER': 'root',
        'PASSWORD': 'bacillus',
        'HOST': 'localhost',   
        'PORT': '3306',
    }
}

