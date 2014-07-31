"""
Django settings for pearl project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import dirname 
BASE_DIR = dirname(dirname(__file__))

from os.path import join 

TEMPLATE_DIRS = (
    join(BASE_DIR, 'apps/home'),
    join(BASE_DIR, 'apps/accounts'),
    join(BASE_DIR, 'apps/project'),
    join(BASE_DIR, 'templates'),
)


MEDIA_ROOT = join(BASE_DIR, 'media')
MEDIA_URL = 'media/'
NEW_PROJECT_DIR = join(MEDIA_URL, 'NewProject/')
REPORT_DIR = join(MEDIA_ROOT, 'Report/')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = join(BASE_DIR, 'collect_static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (join(BASE_DIR, 'static'),)


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
    'registration',
    'debug_toolbar',
    'captcha',
    'djcelery', 
    'kombu.transport.django',
    'django_jenkins',
    'django_shell_ipynb',
    #'django-nose',
    #'guardian',
    'bootstrapform',
    'crispy_forms',
    'bootstrap3',

    #apps
    'apps.home',
    'apps.accounts',
    'apps.project',
    'apps.processing',
    #'vendor.experiment',
    #'vendor.django_celery_example',
)

#login session expiry
SESSION_COOKIE_AGE = 10 * 60

SITE_ID = 1

CRISPY_TEMPLATE_PACK = 'bootstrap3'

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


# Settings for django-celery
import djcelery
djcelery.setup_loader()
BROKER_URL = "django://"
BROKER_BACKEND = 'memory'
CELERY_IMPORTS = ('apps.processing.tasks',)


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

    #'apps.project.middleware.CheckLogin',
    'apps.accounts.middleware.TimezoneMiddleware',
#    'apps.accounts.middleware.EnforceLoginMiddleware',
)

ROOT_URLCONF = 'pearl.urls'

WSGI_APPLICATION = 'pearl.wsgi.application'


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

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# django-guardian
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    'guardian.backends.ObjectPermissionBackend',
)
ANONYMOUS_USER_ID = -1

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

