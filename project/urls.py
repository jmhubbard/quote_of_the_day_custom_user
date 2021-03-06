"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import UserCreate
from django.views.generic.base import TemplateView
from subscriptions.views import SubscriptionUpdate
from main.views import (
    HomePageView, UserLoginView, CustomPasswordResetView, 
    CustomPasswordResetDoneView, CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView, UserLogoutView, CustomPasswordChangeView, CustomPasswordChangeDoneView)

from django.contrib.auth import views as auth_views
from emails.views import ContactView

urlpatterns = [
    path('admin/', admin.site.urls), #admin page
    # path('', TemplateView.as_view(template_name='main/home.html'), name='home'), #Current homepage After logging it you will be redirectedhere
    path('subscriptions/', include('subscriptions.urls')),
    path('accounts/', include('users.urls')),
    path('', HomePageView.as_view(), name='home'),
    # path('accounts/login', UserLoginView.as_view(), name='login'),



    path('reset_password/', CustomPasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('change_password/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('change_password_done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),

    path('contactform', ContactView.as_view(), name='contactform'),
]
