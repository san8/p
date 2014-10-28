from django.db import models
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

#listener must be invoked before sending a signal
from signals import user_registered_callback


class Customer(models.Model):
    user = models.ForeignKey(User, related_name='customer_to_user')
    name = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    timezone = models.CharField(max_length=50, default='', blank=True)

    def __unicode__(self):
        return self.name # pragma: no cover
