from django.conf import settings
from django.core import mail
from django.core.mail import send_mail
from django.test import TestCase


class TestServices(TestCase):

    def test_send_mail(self):
        """
        Test if send mail is working or not.
        """
        subject = 'test subject'
        message = 'message'
        from_mail = settings.DEFAULT_FROM_EMAIL
        to_mails = settings.DEFAULT_TO_EMAIL
        send_mail(subject, message, from_mail, [to_mails])
        self.assertEqual(subject, mail.outbox[0].subject)
