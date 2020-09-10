from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import User
from .forms import UserForm

class UserCreate(CreateView):
    model = User
    form_class = UserForm
    success_url = "/accounts/login/"
