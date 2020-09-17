import os
from django.core.mail import send_mail


def email_test(user):
    send_mail(
        'Test Message',
        'Lets see if this works test',
        os.getenv("EMAIL_HOST_USER"),
        [user],
        fail_silently=False,
)