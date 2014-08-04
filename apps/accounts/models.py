from django.db import models
from django.contrib.auth.models import User #UserManager
from django.dispatch import receiver 
from captcha.fields import CaptchaField 
from registration.signals import user_registered


class Customer(models.Model):
    user = models.ForeignKey(User, related_name='customer_to_user')
    name = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    captcha = CaptchaField()
    timezone = models.CharField(max_length=50, default='', blank=True)

    def __unicode__(self):
        return self.user.username 


@receiver(user_registered)
def user_registered_callback(sender, user, request, **kwargs):
    from .forms import CustomerForm
    form =  CustomerForm(request.POST)
    customer = Customer(user=user)
    customer.name = form.data["name"]
    customer.company = form.data["company"]
    customer.phone_number = form.data["phone_number"]
    customer.save()


