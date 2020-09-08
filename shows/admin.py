from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Show



class ShowAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Show, ShowAdmin)
