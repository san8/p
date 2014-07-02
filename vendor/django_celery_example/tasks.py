from __future__ import absolute_import

from celery.decorators import task 
from celery import shared_task

from .models import SampleCount 


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@task
def add_to_count():
    try:
        sc = SampleCount.objects.get(pk=1)
    except:
        sc = SampleCount()
    sc.num = sc.num + 1
    sc.save()


