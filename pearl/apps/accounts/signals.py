from django.conf import settings
from django.core.mail import send_mail
from django.dispatch import receiver

from allauth.account.signals import user_signed_up


@receiver(user_signed_up)
def send_notification_mail(request, user, **kwargs):
    subject = 'Alert: New User Has Registered'
    message = """
    User details:
    Name: {}
    Email: {}
    """.format(user.username, user.email)
    send_mail(subject, message,
              settings.DEFAULT_FROM_EMAIL,
              settings.DEFAULT_TO_EMAIL)
