from django.db import models
from django.db.models import signals 

from .tasks import start 
from .tasks import add 


def contest_created(sender, instance, created, **kwargs):
    contest_id = instance.id
    start(contest_id)


def start_add(sender, instance, created, **kwargs):
    add.apply_async(args=[1,2])


STATUSES = ((0, 'Not Started'),
            (1, 'Running'),
            (2, 'Completed'),)

class Contest(models.Model):
    status = models.IntegerField(choices=STATUSES, default=0)
    name = models.CharField(max_length=12)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name 


signals.post_save.connect(contest_created, sender=Contest)
signals.post_save.connect(start_add, sender=Contest)




class SampleCount(models.Model):
    num = models.IntegerField(default=0)
