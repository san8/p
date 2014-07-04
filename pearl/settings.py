"""
jango settings for pearl project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from os.path import join 
TEMPLATE_DIRS = (
    join(BASE_DIR, 'apps/home'),
    join(BASE_DIR, 'apps/accounts'),
    join(BASE_DIR, 'apps/project'),
    join(BASE_DIR, 'templates'),
)

STATICFILES_DIRS = (
    join(BASE_DIR, 'static'),
)

MEDIA_ROOT = join(BASE_DIR, 'files')
MEDIA_URL = 'files/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@-+a#8cz=$*c^&jjf9ai!cw976%k!+@v3!%l+j9e%-d#h466*i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # django packages
    'south',
    'django_shell_ipynb',
    'debug_toolbar',
    'registration',

    # for django-celery 
    'djcelery', 
    'kombu.transport.django',

    #'allauth',
    #'allauth.account',
    #'allauth.socialaccount',
    #'bootstrapform',
    #'crispy_forms',
    #'captcha',

    #apps
    'apps.home',
    'apps.accounts',
    'apps.project',

    'vendor.experiment',
    'vendor.django_celery_example',
    'vendor.click_counter', 

)

SITE_ID = 1

CRISPY_TEMPLATE_PACK = 'bootstrap3'

CAPTCHA_LENGTH = 6
#CAPTCHA_WORDS_DICTIONARY = os.path.join(BASE_DIR, 'static') + 'words'


# django-passwords
PASSWORD_MIN_LENGTH = 8
PASSWORD_COMPLEXITY = { # You can ommit any or all of these for no limit for that particular set
    "UPPER": 1,       # Uppercase
    "LOWER": 1,       # Lowercase
    "DIGITS": 1,      # Digits
    #"NON ASCII": 1,   # Non Ascii (ord() >= 128)
    "PUNCTUATION": 1, # Punctuation (string.punctuation)
}


# django-registration - testing
ACCOUNT_ACTIVATION_DAYS = 7
"""
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'testing@example.com'
"""
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'nandapk0@gmail.com'
EMAIL_HOST_PASSWORD = 'nandapk1'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #'apps.project.middleware.CheckLogin',
)

ROOT_URLCONF = 'pearl.urls'

WSGI_APPLICATION = 'pearl.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
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

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


# django-allauth
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    # Required by allauth template tags
    "django.core.context_processors.request",
    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

# add extra fields to signup form
#ACCOUNT_SIGNUP_FORM_CLASS = 'home.forms.SignupFormExtra'
#AUTH_USER_MODEL = 'users.CustomUser' # Mind the syntax here. It's <app>.<model>


# Settings for django-celery
import djcelery
djcelery.setup_loader()
BROKER_URL = "django://"
"""
from vendor import django_celery_example 
django_celery_example.conf.update(
            CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
)
"""
