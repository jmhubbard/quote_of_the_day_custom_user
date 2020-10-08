import os
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.sites.models import Site
from django.template.loader import render_to_string


def email_test(user, message):
    send_mail(
        'Quote test',
        message,
        os.getenv("EMAIL_HOST_USER"),
        [user],
        fail_silently=False,
)

def email_daily_quote(quote, user):
    #Gets the current domain name
    domain = Site.objects.get_current().domain
    # reverse a url in a view to get the path after the domain
    path = reverse('login')
    url = 'http://{domain}{path}'.format(domain=domain, path=path)

    context = {
        "unsubscribe_uri": url,
        "quote": quote,
    }
    message_text = render_to_string("emails/email.txt", context=context)
    message_html = render_to_string("emails/email.html", context=context)
    return send_mail(
        "Quote Of The Day - BETA",
        message_text,
        os.getenv("EMAIL_HOST_USER"),
        [user],
        fail_silently=False,
        html_message=message_html,
    )