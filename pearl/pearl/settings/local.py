"""Additional settings for Development Environment."""

import os 

from .base import *

SECRET_KEY='@-+a#8cz=c^&jjf9ai!cw976%k!+@v3!%l+j9e%-d#h466*i'

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['127.0.0.1',]

INSTALLED_APPS += (
    'debug_toolbar',
    #'django_jenkins',
    #'django_shell_ipynb',
    'django_extensions',
    #'djcelery_testworker',
)

# Database
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

# djceley testrunner
TEST_RUNNER = 'djcelery.contrib.test_runner.CeleryTestSuiteRunner'


