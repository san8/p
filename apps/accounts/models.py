from django.db import models
from django.contrib.auth.models import User #UserManager

from captcha.fields import CaptchaField 
from registration.signals import user_registered


class Customer(models.Model):
    user = models.ForeignKey(User, related_name='customer_to_user')
    name = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    captcha = CaptchaField()

    def __unicode__(self):
        return self.user.username 


from .forms import CustomerForm
def user_registered_callback(sender, user, request, **kwargs):
    form =  CustomerForm(request.POST)
    customer = Customer(user=user)
    customer.name = form.data["name"]
    customer.company = form.data["company"]
    customer.phone_number = form.data["phone_number"]
    customer.save()

user_registered.connect(user_registered_callback)


