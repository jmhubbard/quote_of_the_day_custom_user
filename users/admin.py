from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import UserAdmin
from .models import User

# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('email', 'is_active', 'is_staff','is_superuser', 'date_joined')
#     list_filter = ('is_active','is_staff','is_superuser','date_joined')
#     fieldsets = (
#         (None, {'fields': ('email', 'password',)}),
#         ('Personal info', {'fields': ()}),
#         ('Permissions', {'fields': ('is_active','is_staff','is_superuser',)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2'),
#         }),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()

admin.site.register(User, UserAdmin)

# Register your models here.
