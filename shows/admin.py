from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Show, Episode, Character
from users.models import User
from subscriptions.models import Subscription

from emails.utils import email_all_users_an_email



def create_subscription_for_all_users_if_doesnt_exist(modeladmin, request, queryset):
    all_users = User.objects.all()

    for user in all_users:
        user_shows = user.show_set.all()
        for show in queryset:
            if show not in user_shows:
                # print(f'show is {show} and pref are {user_subscriptions)')
                sub = Subscription(user=user, show=show)
                sub.save()

def make_show_active(modeladmin, request, queryset):
    for show in queryset:
        show.is_active = True
        show.save()

def make_show_inactive(modeladmin, request, queryset):
    for show in queryset:
        show.is_active = False
        show.save()

def email_users_about_new_show(modeladmin, request, queryset):
    all_users = User.objects.all()

    for user in all_users:
        email_all_users_an_email(user, queryset)


class ShowAdmin(admin.ModelAdmin):
    actions = (
    create_subscription_for_all_users_if_doesnt_exist,
    make_show_active,
    make_show_inactive,
    email_users_about_new_show,
    )
    
    list_display = ('name','is_active','subscriber_count')

    def subscriber_count(self, show):
        user_count = Show.objects.filter(subscription__status = 1, name = show)
        return user_count.count()

class EpisodeAdmin(admin.ModelAdmin):

    list_display = ('name', 'season', 'show')

class CharacterAdmin(admin.ModelAdmin):

    list_display = ('__str__','first_name', 'last_name','show')


admin.site.register(Show, ShowAdmin)

admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Character, CharacterAdmin)
# admin.site.register(Character)