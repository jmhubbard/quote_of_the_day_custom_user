from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Show, Episode, Character
from users.models import User
from subscriptions.models import Subscription



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


class ShowAdmin(admin.ModelAdmin):
    actions = (
    create_subscription_for_all_users_if_doesnt_exist,
    make_show_active,
    make_show_inactive,
    )
    
    list_display = ('name','is_active','subscriber_count')

    def subscriber_count(self, show):
        user_count = Show.objects.filter(subscription__status = 1, name = show)
        return user_count.count()

class EpisodeAdmin(admin.ModelAdmin):

    list_display = ('name','season','number','show')

class CharacterAdmin(admin.ModelAdmin):

    list_display = ('name','show')


admin.site.register(Show, ShowAdmin)

admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Character, CharacterAdmin)