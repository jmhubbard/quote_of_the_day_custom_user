from django.contrib import admin
from .models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'show', 'is_subscribed')
admin.site.register(Subscription, SubscriptionAdmin)