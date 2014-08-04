from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@-+a#8cz=$*c^&jjf9ai!cw976%k!+@v3!%l+j9e%-d#h466*i'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += (
    'south',
    'debug_toolbar',
    'django_jenkins',
    'django_shell_ipynb',

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

# django-nose
#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
# djceley testrunner
TEST_RUNNER = 'djcelery.contrib.test_runner.CeleryTestSuiteRunner'

# public urls for enfore login middle ware
PUBLIC_URLS = (
    r'/',
    r'/home/',
    r'/home/faq/',
    r'/accounts/register/',
    r'/accounts/login/',
)
SERVE_STATIC_TO_PUBLIC = True 


#LOGIN_URL = 'accounts/login'
#LOGIN_REDIRECT_URL = 'accounts/dashboard'

#celery - depricated pickle
#CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
