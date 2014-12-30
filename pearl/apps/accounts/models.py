from django.db import models
from django.contrib.auth.models import User
from paypal.standard.ipn.models import PayPalIPN

#listener must be invoked before sending a signal
from .signals import user_registered_callback


class Customer(models.Model):
    """
    Store customer details.
    """
    user = models.ForeignKey(User, related_name='customer_to_user')
    name = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    timezone = models.CharField(max_length=50, default='', blank=True)
    balance = models.FloatField(default=0.0)

    def __unicode__(self):
        return self.name # pragma: no cover


class Payment(models.Model):
    """
    Table to map paypal transactions & user_id.
    """
    user = models.ForeignKey(User, related_name='payments_to_user')
    payment = models.ForeignKey(PayPalIPN, related_name='paypal_id')
