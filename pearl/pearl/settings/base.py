"""
Django settings for pearl project.
"""

from os.path import join, dirname, abspath

CURRENT_DIR = abspath(join(dirname( __file__ ), '..'))
BASE_DIR = abspath(join(CURRENT_DIR, '..'))


# Static and media
STATICFILES_DIRS = (
    join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = (
    join(BASE_DIR, 'apps/home'),
    join(BASE_DIR, 'apps/accounts'),
    join(BASE_DIR, 'apps/project'),
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
    'djcelery', 
    'kombu.transport.django',
    'bootstrapform',
    #'chartkick',
    #'bootstrap3',
    'crispy_forms',
    'floppyforms',

    #apps
    'apps.home',
    'apps.accounts',
    'apps.project',
    'apps.processing',
)

#For django-crispy-froms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

#login session expiry
SESSION_COOKIE_AGE = 10 * 60

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

 #   'common.middleware.LoginRequiredMiddleware',
#    'common.middleware.RequireLoginMiddleware',
    #'apps.accounts.middlewares.TimezoneMiddleware',
    #'apps.project.middleware.CheckLogin',
    #'apps.accounts.middleware.EnforceLoginMiddleware',
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


# django-guardian
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    'guardian.backends.ObjectPermissionBackend',
)
ANONYMOUS_USER_ID = -1

