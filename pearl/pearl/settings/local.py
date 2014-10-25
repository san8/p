"""Additional settings for Development Environment."""

import os 

from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',]

INSTALLED_APPS += (
    'debug_toolbar',
    'django_jenkins',
    'django_shell_ipynb',
    'django_extensions',
    #'djcelery_testworker',
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pearl',
        'USER': 'root',
        'PASSWORD': 'pearl',
        'HOST': 'localhost',   
        'PORT': '3306',
    }
}

#import dj_database_url
#DATABASES['default'] = dj_database_url.config(default='mysql://db/pearl.db')

# django-nose
#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
# djceley testrunner
TEST_RUNNER = 'djcelery.contrib.test_runner.CeleryTestSuiteRunner'


#LOGIN_URL = 'accounts/login'
#LOGIN_REDIRECT_URL = 'accounts/dashboard'
