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
from django.urls import path, include
from users.views import UserCreate
from main.views import UserLoginView, UserLogoutView

# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('add/', UserCreate.as_view(), name='user-add'), #Create user page
    path('logout/' , UserLogoutView.as_view(), name='logout')
        # path('', include('django.contrib.auth.urls')), #accounts/login = login page
        # path('accounts/', include('django.contrib.auth.urls')), #accounts/login = login page
]
