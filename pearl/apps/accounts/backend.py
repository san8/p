"""
from registration.signals import user_registered

from .models import Customer 
from .forms import CustomerForm


def user_registered_callback(sender, user, request, **kwargs):
    form =  CustomerForm(request.POST)
    customer = Customer(user=user)
    customer.company = form.data["company"]
    customer.save()


user_registered.connect(user_registered_callback)
from .models import Customer 
from registration.signals import user_registered
from .forms import CustomerForm

@user_registered 
def user_registered_callback(sender, user, request, **kwargs):
    form =  CustomerForm(request.POST)
    customer = Customer(user=user)
    customer.company = form.data["company"]
    customer.save()


user_registered.connect(user_registered_callback)
"""
