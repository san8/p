from __future__ import absolute_import

from os import environ

from celery import Celery
from django.conf import settings


environ.setdefault('DJANGO_SETTINGS_MODULE', 'pearl.settings.local')

app = Celery('pearl', broker='amqp://', backend='amqp://',
             include=['apps.project.tasks', 'apps.processing.tasks'],)

app.conf.update(
    CELERYD_POOL_RESTARTS=True,
    CELERY_ENABLE_UTC=True,
    CELERY_TIMEZONE="UTC",
)

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
