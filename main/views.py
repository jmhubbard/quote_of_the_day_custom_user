from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from main.decorators import unauthenticated_user
from django.contrib.auth.views import (LoginView, 
PasswordResetView, PasswordResetDoneView, 
PasswordResetConfirmView, PasswordResetCompleteView)




class HomePageView(TemplateView):

    template_name = "main/home.html"

    @method_decorator(unauthenticated_user) #If user is already authenticated they will be redirected to their subscription page
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class UserLoginView(LoginView):

    template_name = "registration/login.html"

    @method_decorator(unauthenticated_user) #If user is already authenticated they will be redirected to their subscription page
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CustomPasswordResetView(PasswordResetView):

    template_name = "main/password_reset.html"

    @method_decorator(unauthenticated_user) #If user is already authenticated they will be redirected to their subscription page
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CustomPasswordResetDoneView(PasswordResetDoneView):

    template_name = "main/password_reset_sent.html"

    @method_decorator(unauthenticated_user) #If user is already authenticated they will be redirected to their subscription page
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CustomPasswordResetConfirmView(PasswordResetConfirmView):

    template_name = "main/password_reset_form.html"

    @method_decorator(unauthenticated_user) #If user is already authenticated they will be redirected to their subscription page
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CustomPasswordResetCompleteView(PasswordResetCompleteView):

    template_name = "main/password_reset_done.html"

    @method_decorator(unauthenticated_user) #If user is already authenticated they will be redirected to their subscription page
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)