from django.dispatch import receiver
from django.core.mail import send_mail

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

    # send additional mail to info
    message = """
    User details:
    Name: {0}
    Email: {1}
    Phone Number: {2}
    """.format(user.first_name, user.email, customer.phone_number)
    
    send_mail('New User Has Registered', message,
              'noreply@leucinerichbio.com',
              ['info@leucinerichbio.com',])

