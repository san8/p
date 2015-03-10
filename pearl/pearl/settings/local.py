"""
Additional settings for Development Environment.
"""

import os

from .base import *  # noqa

SECRET_KEY = os.environ.get('SECRET_KEY', '')

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['127.0.0.1']


INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
    'django_jenkins',
)


# Database
DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pearl',
        'USER': os.environ.get('DB_USER', None),
        'PASSWORD': os.environ.get('DB_PASS', None),
        'HOST':  os.environ.get('DB_HOST', None),
        'PORT':  os.environ.get('DB_PORT', None),
    },

    'reports': {
        'NAME': 'project_reports',
        'ENGINE': 'django.db.backends.mysql',
        'USER': os.environ.get('REPORTS_DB_USER', None),
        'PASSWORD': os.environ.get('REPORTS_DB_PASS', None),
        'HOST':  os.environ.get('REPORTS_DB_HOST', None),
        'PORT':  os.environ.get('REPORTS_DB_PORT', None),
    }

}

EMAIL_HOST = os.environ.get('EMAIL_HOST', None)
EMAIL_PORTHOST = os.environ.get('EMAIL_PORT', None)
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', None)
SECURITY_EMAIL_SENDER = os.environ.get('SECURITY_EMAIL_SENDER', None)
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', None)
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', None)
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', None)
DEFAULT_TO_EMAIL = [os.environ.get('DEFAULT_TO_EMAIL', None)]


# jenkins
PROJECT_APPS = (
    'apps.base',
)

JENKINS_TASKS = (
    'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_flake8',
    'django_jenkins.tasks.run_pyflakes',
    # 'django_jenkins.tasks.run_jslint',
    # 'django_jenkins.tasks.run_csslint',
)
