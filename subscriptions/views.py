from django.shortcuts import render

from django.views.generic.edit import UpdateView
from .models import Subscription
from .forms import SubscriptionForm
# from.django.core.urlresolvers import reverse_lazy

class SubscriptionUpdate(UpdateView):
    model = Subscription
    form_class = SubscriptionForm
    # fields = ['user','show','is_subscribed',]
    # template_name_suffix = 'subscriptionupdate.html'
