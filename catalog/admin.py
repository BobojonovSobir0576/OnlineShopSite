from django.contrib import admin
from catalog import models as m

@admin.register(m.Product)
class Product(admin.ModelAdmin):
    list_display = [field.name for field in m.Product._meta.fields]

    class Meta:
        model = m.Product

@admin.register(m.Brands)
class Brands(admin.ModelAdmin):
    list_display = [field.name for field in m.Brands._meta.fields]

    class Meta:
        model = m.Brands

@admin.register(m.Models)
class Models(admin.ModelAdmin):
    list_display = [field.name for field in m.Models._meta.fields]

    class Meta:
        model = m.Models

@admin.register(m.Seasson)
class Seasson(admin.ModelAdmin):
    list_display = [field.name for field in m.Seasson._meta.fields]

    class Meta:
        model = m.Seasson

@admin.register(m.CarTypes)
class CarTypes(admin.ModelAdmin):
    list_display = [field.name for field in m.CarTypes._meta.fields]

    class Meta:
        model = m.CarTypes

@admin.register(m.CountryManufacter)
class CountryManufacter(admin.ModelAdmin):
    list_display = [field.name for field in m.CountryManufacter._meta.fields]

    class Meta:
        model = m.CountryManufacter

@admin.register(m.GuideCharacteristic)
class GuideCharacteristic(admin.ModelAdmin):
    list_display = [field.name for field in m.GuideCharacteristic._meta.fields]

    class Meta:
        model = m.GuideCharacteristic

@admin.register(m.GuideUnitsMeasurement)
class GuideUnitsMeasurement(admin.ModelAdmin):
    list_display = [field.name for field in m.GuideUnitsMeasurement._meta.fields]

    class Meta:
        model = m.GuideUnitsMeasurement

@admin.register(m.SetCharesteristicProduct)
class SetCharesteristicProduct(admin.ModelAdmin):
    list_display = [field.name for field in m.SetCharesteristicProduct._meta.fields]

    class Meta:
        model = m.SetCharesteristicProduct