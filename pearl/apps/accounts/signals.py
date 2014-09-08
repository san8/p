from django.dispatch import receiver
from registration.signals import user_registered


@receiver(user_registered)
def user_registered_callback(sender, user, request, **kwargs):
    from .forms import CustomerForm
    from .models import Customer
    form =  CustomerForm(request.POST)
    customer = Customer(user=user)
    customer.name = form.data["name"]
    customer.company = form.data["company"]
    customer.phone_number = form.data["phone_number"]
    customer.save()


