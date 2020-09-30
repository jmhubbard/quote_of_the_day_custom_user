import string

from django import forms
from django.forms import ModelForm

from .models import User, make_random_username

from subscriptions.models import Subscription, subscribe_user_on_creation

from shows.models import Show

from django.contrib.auth.password_validation import validate_password

from emails.models import create_email_tracker_for_user_on_creation

class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    # username = forms.CharField(hidden=True)
    class Meta:
        model = User
        fields = ('email',)
        exclude = ['username',]

    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        validate_password(password2)
        return password2

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.username = self.make_random_username()
        user.set_password(self.cleaned_data["password2"])
        user.save()
        shows = Show.objects.all()
        subscribe_user_on_creation(user, shows) ## Creates a subscription to each show in database for new user. 
        create_email_tracker_for_user_on_creation(user)
        return user

    def make_random_username(self):
        return make_random_username(length=14, allowed_chars=string.ascii_lowercase)