from django.contrib import admin
from .models import Subscription



class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'show', 'status')
    list_filter = ('show','status',)

admin.site.register(Subscription, SubscriptionAdmin)