from django.contrib import admin

from profiles.models import Staff


@admin.register(Staff)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user', )