from django.contrib import admin
from .models import *

@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

    class Meta:
        model = Order