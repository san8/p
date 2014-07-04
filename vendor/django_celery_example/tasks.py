from __future__ import absolute_import

import time 

from celery.decorators import task 
#from celery import shared_task
#from .models import SampleCount 
#from .models import Contest 


@task
def add(x, y):
    return x + y


@task(ignore_result=True)
def substract(x, y):
    return x - y 

@task
def start(contest_id, **kwargs):
    pass 


"""
@task
def start(contest_id, **kwargs):
    contest = Contest.objects.get(id=contest_id)
    contest.status = 1
    contest.save()
    time.sleep(5)
    end.apply_async(args=[contest_id,], eta=contest.end_date)
    #task = end.apply_async(args=[contest_id,], eta=contest.end_date)


@task 
def end(contest_id, **kwargs):
    contest = Contest.objects.get(id=contest_id)
    contest.status = 2
    contest.save()




"""

"""
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

"""

