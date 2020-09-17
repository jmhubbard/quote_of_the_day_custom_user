from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import User
from .forms import UserForm
from django.contrib.messages.views import SuccessMessageMixin
from main.decorators import unauthenticated_user
from django.utils.decorators import method_decorator


class UserCreate(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    success_url = "/accounts/login/"
    success_message = "Account was successfully created."

    @method_decorator(unauthenticated_user) #If user is already authenticated they will be redirected to their subscription
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
