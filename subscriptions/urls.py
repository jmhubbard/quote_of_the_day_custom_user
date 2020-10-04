
from django.urls import path, include
from . import views
from subscriptions.views import SubscriptionUpdate

urlpatterns = [
    path('', views.subscription, name='subscriptions'), #Main user subscription page
    path('update/<int:pk>/', SubscriptionUpdate.as_view(), name = 'subscription-update'), #Each show subscription page
]