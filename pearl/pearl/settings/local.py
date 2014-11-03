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
    'djcelery_testworker',
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

# djcelery testrunner
TEST_RUNNER = 'djcelery.contrib.test_runner.CeleryTestSuiteRunner'


# email settings
EMAIL_HOST = 'mail.leucinerichbio.com'
EMAIL_PORT = 26
EMAIL_HOST_USER = 'noreply@leucinerichbio.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS', '')
DEFAULT_FROM_EMAIL = 'noreply@leucinerichbio.com'
DEFAULT_TO_EMAIL = 'noreply@leucinerichbio.com'
