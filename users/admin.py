from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'position', 'department', 'phone']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'position', 'department', 'phone')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'position', 'department', 'phone')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
