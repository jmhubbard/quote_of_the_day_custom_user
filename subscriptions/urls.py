
from django.urls import path, include
from . import views
from subscriptions.views import SubscriptionUpdate

urlpatterns = [
    path('', views.subscription, name='account_page'), #Main user subscription page
    path('update/<int:pk>/', SubscriptionUpdate.as_view(), name = 'subscription-update'), #Each show subscription page
]