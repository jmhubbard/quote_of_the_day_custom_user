from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Show
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


class ShowAdmin(admin.ModelAdmin):
    actions = (
    create_subscription_for_all_users_if_doesnt_exist,
    )
    list_display = ('name',)

admin.site.register(Show, ShowAdmin)
