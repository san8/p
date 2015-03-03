from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from paypal.standard.ipn.models import PayPalIPN
from paypal.standard.ipn.signals import payment_was_successful


class Customer(models.Model):
    """
    Store customer details.
    """
    user = models.ForeignKey(User, related_name='customer_to_user')
    salutation = models.CharField(max_length=10, blank=True)
    company = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    timezone = models.CharField(max_length=50, default='', blank=True)
    balance = models.FloatField(default=0.0)

    def __unicode__(self):
        return self.user.email  # pragma: no cover


class Payment(models.Model):
    """
    Table to map paypal transactions & user_id.
    """
    user = models.ForeignKey(User, related_name='payments_to_user')
    payment = models.ForeignKey(PayPalIPN, related_name='paypal_id')


@receiver(payment_was_successful)
def update_payment_info(sender, **kwargs):
    paypal_object = sender
    amount = paypal_object.mc_gross
    user_id = paypal_object.custom
    customer = Customer.objects.get(user_id=user_id)
    customer.balance += float(amount)
    customer.save()


class Discount(models.Model):
    """
    Table for user specific discounts
    """
    user = models.OneToOneField(User)
    fastq = models.FloatField(default=0.0)
    vcf = models.FloatField(default=0.0)

    def __unicode__(self):
        return self.user.username  # pragma: no cover
