from django.conf import settings
from django.core import mail
from django.core.mail import send_mail


def test_send_mail():
    """
    Test if send mail is working or not.
    """
    subject = 'test subject'
    message = 'message'
    from_mail = settings.DEFAULT_FROM_EMAIL
    to_mails = [settings.DEFAULT_TO_EMAIL]
    send_mail(subject, message, from_mail, to_mails)
    assert subject == mail.outbox[0].subject
