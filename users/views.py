from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import User
from .forms import UserForm
from django.contrib.messages.views import SuccessMessageMixin


class UserCreate(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    success_url = "/accounts/login/"
    success_message = "Account was successfully created."
