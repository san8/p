"""
Django settings for pearl project.
"""

import os
from os.path import join, dirname, abspath

CURRENT_DIR = abspath(join(dirname(__file__), '..'))
BASE_DIR = abspath(join(CURRENT_DIR, '..'))


# Static and media
STATICFILES_DIRS = (
    join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = (
    join(BASE_DIR, 'apps/home/templates/'),
    join(BASE_DIR, 'apps/accounts/templates/'),
    join(BASE_DIR, 'apps/accounts/templates/registration'),
    join(BASE_DIR, 'apps/project/templates/'),
)

STATIC_ROOT = join(BASE_DIR, 'collect_static')
STATIC_URL = '/static/'

MEDIA_ROOT = join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

NEW_PROJECT_DIR = join(MEDIA_ROOT, 'NewProject/')
NEW_PROJECT_URL = join(MEDIA_URL, 'NewProject/')


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
    'registration',
    'captcha',
    'kombu.transport.django',
    'bootstrapform',
    'crispy_forms',
    'floppyforms',
    'billing',
    'paypal.standard',
    'paypal.pro',
    'paypal.standard.pdt',
    'paypal.standard.ipn',
    'prompt_toolkit',

    #apps
    'apps.home',
    'apps.accounts',
    'apps.project',
    'apps.processing',
)

#For django-crispy-froms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

#login session expiry
SESSION_COOKIE_AGE = 15 * 60

SITE_ID = 1


# django-captcha
CAPTCHA_LENGTH = 6
#CAPTCHA_WORDS_DICTIONARY = join(BASE_DIR, 'static') + 'words'


# django-passwords
PASSWORD_MIN_LENGTH = 8
PASSWORD_COMPLEXITY = {
    # You can ommit any or all of these for no limit for that particular set
    "UPPER": 1,       # Uppercase
    "LOWER": 1,       # Lowercase
    "DIGITS": 1,      # Digits
    #"NON ASCII": 1,   # Non Ascii (ord() >= 128)
    "PUNCTUATION": 1, # Punctuation (string.punctuation)
}


# django-registration
ACCOUNT_ACTIVATION_DAYS = 3


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

ROOT_URLCONF = 'pearl.urls'

WSGI_APPLICATION = 'pearl.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ANONYMOUS_USER_ID = -1


# django-paypal
PAYPAL_WPP_USER = os.environ.get('PAYPAL_WPP_USER')
PAYPAL_WPP_PASSWORD = os.environ.get('PAYPAL_WPP_PASSWORD')
PAYPAL_WPP_SIGNATURE = os.environ.get('PAYPAL_WPP_SIGNATURE')
PAYPAL_RECEIVER_EMAIL = os.environ.get('PAYPAL_RECEIVER_EMAIL')


# django merchant
MERCHANT_TEST_MODE = os.environ.get('MERCHANT_TEST_MODE')
PAYPAL_TEST = MERCHANT_TEST_MODE
MERCHANT_SETTINGS = {
    "pay_pal": {
        'WPP_USER': os.environ.get('WPP_USER'),
        'WPP_PASSWORD': os.environ.get('WPP_PASSWORD'),
        'WPP_SIGNATURE': os.environ.get('WPP_SIGNATURE'),
        'RECEIVER_EMAIL': os.environ.get('RECEIVER_EMAIL'),
    }
}
PAYPAL_IDENTITY_TOKEN = os.environ.get('PAYPAL_IDENTITY_TOKEN')


# admins
ADMINS = (
    (os.environ.get('ADMIN_NAME'), os.environ.get('ADMIN_EMAIL'))
)


# pearl settings
# payment settings
VCF_COST = 25.00
FASTQ_COST = 150.00


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },

    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', ],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['file', ],
        },
    }
}
