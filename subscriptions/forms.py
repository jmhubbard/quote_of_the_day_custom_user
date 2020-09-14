from django import forms
from subscriptions.models import Subscription

class SubscriptionForm(forms.ModelForm):
 

    class Meta:
        model = Subscription
        fields = [
            'show',
            'subscription_preference',
            ]
    def save(self, commit=True):
        usersubscription = super().save(commit=False)
        # user = User.objects.get(username = "jasonhubb@gmail.com")
        usersubscription.show = self.cleaned_data['show']
        usersubscription.is_subscribed = self.cleaned_data['subscription_preference']

        # userpreference.user = user
        if commit:
            usersubscription.save()
        return usersubscription
