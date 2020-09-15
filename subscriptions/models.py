from django.db import models
import users.models
import shows.models
from django import forms
from django.utils.translation import gettext as _

def subscribe_user_on_creation(user, shows):
    for show in shows:
        subscription = Subscription()
        subscription.user = user
        subscription.show = show
        subscription.save()
    


subscription_choices = (
    ('Subscribed', 'Subscribed'),
    ('Unsubscribed', 'Unsubscribed')
)

class Subscription(models.Model):
    STATUS_CHOICE_UNKNOWN = 0
    STATUS_CHOICE_SUBSCRIBED = 1
    STATUS_CHOICE_UNSUBSCRIBED = 2
    STATUS_CHOICES = (
        (STATUS_CHOICE_UNKNOWN, _('Unknown')),
        (STATUS_CHOICE_SUBSCRIBED, _('Subscribed')),
        (STATUS_CHOICE_UNSUBSCRIBED, _('Unsubscribed')),

    )

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    show = models.ForeignKey('shows.Show', on_delete=models.CASCADE)
    status = models.IntegerField( 
        choices = STATUS_CHOICES, 
        default = STATUS_CHOICE_SUBSCRIBED,
        ) 

    class Meta:
        unique_together = (
            ("user", "show"),
        )

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("subscription-update", args=[self.id])

    def __str__(self):
        return (f'{self.user}    {self.show}    {self.status}')