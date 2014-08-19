from __future__ import absolute_import

from os import environ
from celery import Celery

from django.conf import settings


# set the default Django settings module for the 'celery' program.
environ.setdefault('DJANGO_SETTINGS_MODULE', 'pearl.settings')

app = Celery('pearl')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


