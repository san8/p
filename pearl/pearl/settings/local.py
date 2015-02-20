"""
Additional settings for Development Environment.
"""

import os

from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY', '')

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['127.0.0.1',]

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
    'djsupervisor',
)


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pearl',
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASS', ''),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_PORTHOST = os.environ.get('EMAIL_PORT', '')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', '')
SECURITY_EMAIL_SENDER = os.environ.get('SECURITY_EMAIL_SENDER', '')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', '')
DEFAULT_TO_EMAIL = os.environ.get('DEFAULT_TO_EMAIL', '')
