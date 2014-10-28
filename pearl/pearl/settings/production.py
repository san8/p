"""Additional settings for Development Environment."""

import os 

from .base import *

SECRET_KEY='@-+a#8cz=c^&jjf9ai!cw976%k!+@v3!%l+j9e%-d#h466*i'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',]

INSTALLED_APPS += (
    #'debug_toolbar',
    #'django_jenkins',
    #'django_shell_ipynb',
    'django_extensions',
    #'djcelery_testworker',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pearl',
        'USER': 'root',
        'PASSWORD': 'bacillus123',
        'HOST': 'localhost',   
        'PORT': '3306',
    }
}

# djceley testrunner
TEST_RUNNER = 'djcelery.contrib.test_runner.CeleryTestSuiteRunner'


EMAIL_HOST = 'mail.leucinerichbio.com'
EMAIL_PORT = 26
EMAIL_HOST_USER = 'noreply@leucinerichbio.com'
EMAIL_HOST_PASSWORD = 'reply123'
