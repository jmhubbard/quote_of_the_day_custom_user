import os
from django.core.mail import send_mail


def email_test(user, message):
    send_mail(
        'Quote test',
        message,
        os.getenv("EMAIL_HOST_USER"),
        [user],
        fail_silently=False,
)