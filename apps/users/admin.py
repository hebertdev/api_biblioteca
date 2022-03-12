"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

# Models
from apps.users.models import User, Profile


class CustomUserAdmin(UserAdmin):
    """User model admin."""
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_manager')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (None, {'fields': ('is_manager',)}),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin."""
    list_display = ('user',)
  


admin.site.register(User, CustomUserAdmin)