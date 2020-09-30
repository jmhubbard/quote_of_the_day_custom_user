from django.contrib import admin
from emails.models import EmailTracker

class EmailTrackerAdmin(admin.ModelAdmin):

    list_display = ('user', 'last_quote_email')


admin.site.register(EmailTracker, EmailTrackerAdmin)