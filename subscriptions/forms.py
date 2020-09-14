from django import forms
from subscriptions.models import Subscription
from django.utils.translation import gettext as _

class SubscriptionForm(forms.ModelForm):
    # class LimitedStatus:
    #     Subscription.Status.SUBSCRIBED
    #     Subscription.Status.UNSUBSCRIBED
    STATUS_CHOICES = (
        (Subscription.STATUS_CHOICE_SUBSCRIBED, _('Subscribed')),
        (Subscription.STATUS_CHOICE_UNSUBSCRIBED, _('Unsubscribed')),
    )

    status =  forms.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model = Subscription
        fields = [
            'status',
            # 'status2'
            ]
    def save(self, commit=True):
        usersubscription = super().save(commit=False)
        usersubscription.status = self.cleaned_data['status']

        # userpreference.user = user
        if commit:
            usersubscription.save()
        return usersubscription
