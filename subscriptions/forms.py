from django import forms
from subscriptions.models import Subscription
from django.utils.translation import gettext as _

class SubscriptionForm(forms.ModelForm):
    #STATUS_CHOICES IS SET TO BE LIKE STATUS_CHOICES IN SUBSCRIPTION MODEL BUT WITHOUT UKNOWN AND (UNKOWN) FOR USERS TO SELECT
    STATUS_CHOICES = (
        (Subscription.STATUS_CHOICE_SUBSCRIBED, _('Subscribed')),
        (Subscription.STATUS_CHOICE_UNSUBSCRIBED, _('Unsubscribed')),
    )

    status =  forms.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model = Subscription
        fields = [
            'status',
            ]
    def save(self, commit=True):
        usersubscription = super().save(commit=False)
        usersubscription.status = self.cleaned_data['status']

        if commit:
            usersubscription.save()
        return usersubscription
