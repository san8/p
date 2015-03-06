"""
Django settings for pearl project.
"""

import os
from os.path import join


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Static and media
STATICFILES_DIRS = (
    join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = (
    join(BASE_DIR, 'templates/'),
    join(BASE_DIR, 'apps/home/templates/'),
    join(BASE_DIR, 'apps/accounts/templates/'),
    join(BASE_DIR, 'apps/accounts/templates/registration'),
    join(BASE_DIR, 'apps/project/templates/'),
)

STATIC_ROOT = join(BASE_DIR, 'collect_static')
STATIC_URL = '/static/'

MEDIA_ROOT = join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

PROJECTS_PATH = 'projects/'
PROJECTS_DIR = join(MEDIA_ROOT, 'projects/')
PROJECTS_URL = join(MEDIA_URL, PROJECTS_PATH)


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'apps.accounts',

    'allauth',
    'allauth.account',
    'bootstrapform',
    'bootstrap3',
    'billing',
    'paypal.standard',
    'paypal.pro',
    'paypal.standard.pdt',
    'paypal.standard.ipn',

    # apps
    'apps.base',
    'apps.home',
    'apps.project',
    'apps.processing',
)


# login session expiry
SESSION_COOKIE_AGE = 15 * 60

SITE_ID = 1


# allauth
TEMPLATE_CONTEXT_PROCESSORS = (
    # Required by allauth template tags
    "django.core.context_processors.request",
    "django.core.context_processors.csrf",
    "django.contrib.auth.context_processors.auth",
    # allauth specific context processors
    "allauth.account.context_processors.account",
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[AGIS] "
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_SIGNUP_FORM_CLASS = 'apps.accounts.forms.SignupForm'
ACCOUNT_ADAPTER = "apps.accounts.adapter.CustomAccountAdapter"


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pearl.urls'

WSGI_APPLICATION = 'pearl.wsgi.application'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_L10N = True

USE_TZ = True

ANONYMOUS_USER_ID = -1


# django-paypal
PAYPAL_WPP_USER = os.environ.get('PAYPAL_WPP_USER', None)
PAYPAL_WPP_PASSWORD = os.environ.get('PAYPAL_WPP_PASSWORD', None)
PAYPAL_WPP_SIGNATURE = os.environ.get('PAYPAL_WPP_SIGNATURE', None)
PAYPAL_RECEIVER_EMAIL = os.environ.get('PAYPAL_RECEIVER_EMAIL', None)


# django merchant
MERCHANT_TEST_MODE = os.environ.get('MERCHANT_TEST_MODE', None)
PAYPAL_TEST = MERCHANT_TEST_MODE
MERCHANT_SETTINGS = {
    "pay_pal": {
        'WPP_USER': os.environ.get('WPP_USER', None),
        'WPP_PASSWORD': os.environ.get('WPP_PASSWORD', None),
        'WPP_SIGNATURE': os.environ.get('WPP_SIGNATURE', None),
        'RECEIVER_EMAIL': os.environ.get('RECEIVER_EMAIL', None),
    }
}
PAYPAL_IDENTITY_TOKEN = os.environ.get('PAYPAL_IDENTITY_TOKEN', None)


# admins
ADMINS = (
    (os.environ.get('ADMIN_NAME', None), os.environ.get('ADMIN_EMAIL', None)),
)


# pearl settings
# payment settings
VCF_COST = 25.00
FASTQ_COST = 150.00


# django recaptcha
NORECAPTCHA_SITE_KEY = '6LdXoAITAAAAAAniBwAnUMHudBTYwA-p7acuNuCa'
NORECAPTCHA_SECRET_KEY = '6LdXoAITAAAAAHs3RvuFN5MokpBsVsvFxLZC8qUF'


# django crispy_forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'
