from django.contrib import admin
from .models import Subscription

def subscribe_to_selected_shows(modeladmin, request, queryset):
    for subscription in queryset:
        subscription.status = 1
        subscription.save()

def unsubscribe_to_selected_shows(modeladmin, request, queryset):
    for subscription in queryset:
        subscription.status = 2
        subscription.save()

class SubscriptionAdmin(admin.ModelAdmin):
    actions = (
        subscribe_to_selected_shows,
        unsubscribe_to_selected_shows,
    )

    list_display = ('user', 'show', 'status')
    list_filter = ('show','status',)

admin.site.register(Subscription, SubscriptionAdmin)