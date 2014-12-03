from __future__ import absolute_import

from os import environ
from celery import Celery

from django.conf import settings



# set the default Django settings module for the 'celery' program.
environ.setdefault('DJANGO_SETTINGS_MODULE', 'pearl.settings')

app = Celery('pearl', broker='amqp://', backend='amqp://',
             include=['apps.project.tasks', 'apps.processing.tasks'],)

app.conf.update(
    CELERYD_POOL_RESTARTS = True,
    CELERY_TASK_SERIALIZER = 'json',
    CELERY_RESULT_SERIALIZER = 'json',
    CELERY_ACCEPT_CONTENT = ['json'],
    CELERY_ENABLE_UTC = True,
    CELERY_TIMEZONE = "UTC",
)


# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)



CELERY_TIMEZONE = 'UTC'
