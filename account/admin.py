from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

from account.forms import CustomUserCreationForm, CustomUserChangeForm
from account.models import *

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', 'email', 'is_active',
                    'last_name', 'first_name', 'gender',)
    list_filter = ('groups', 'is_active', 'is_superuser', 'gender', 'birthdate',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email', 'phone_number',
         'first_name', 'last_name', 'gender', 'birthdate', 'photo')}),
        (_('Permissions'), {'fields': (
            'is_active', 'is_superuser', 'is_staff', 'groups', 'user_permissions',)}),
        (_('Additional info'), {'fields': ('last_login', 'date_joined',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2',)}
         ),
        (_('Permissions'), {
            'fields': ('is_superuser', 'is_staff',)
        })
    )
    search_fields = ('username', 'email', 'last_name', 'first_name')
    ordering = ('last_name', 'first_name')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Gender)