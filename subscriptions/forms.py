from django import forms
from subscriptions.models import Subscription

class SubscriptionForm(forms.ModelForm):
 

    class Meta:
        model = Subscription
        fields = [
            'show',
            'is_subscribed',
            ]
    def save(self, commit=True):
        usersubscription = super().save(commit=False)
        # user = User.objects.get(username = "jasonhubb@gmail.com")
        usersubscription.show = self.cleaned_data['show']
        usersubscription.is_subscribed = self.cleaned_data['is_subscribed']

        # userpreference.user = user
        if commit:
            usersubscription.save()
        return usersubscription
