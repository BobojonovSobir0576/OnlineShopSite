from django.db import models
from django.urls import reverse
from utils.utils import *

class Seasson(models.Model):
    seasson = models.CharField(max_length=64, validators=[validate])
    class Meta:
        verbose_name = 'Сезон'
        verbose_name_plural = 'Сезоны'
    def __str__(self):
        return self.seasson

class CarTypes(models.Model):
    type = models.CharField(max_length=64, validators=[validate])
    class Meta:
        verbose_name = 'Тип машины'
        verbose_name_plural = 'Типы Машин'
    def __str__(self):
        return self.type

class CountryManufacter(models.Model):
    name = models.CharField(max_length=64, validators=[validate])
    class Meta:
        verbose_name = 'Страны производителей'
        verbose_name_plural = 'Страна производителя'
    def __str__(self):
        return self.name

class Brands(models.Model):
    name = models.CharField(max_length=64, validators=[validate])
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
    def __str__(self):
        return self.name

class Models(models.Model):
    brand = models.ForeignKey(Brands, on_delete=models.PROTECT, related_name='brandmodel', verbose_name='Бренд')
    name = models.CharField(max_length=64, validators=[validate])
    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модель'
    def __str__(self):
        return self.name

class GuideCharacteristic(models.Model):
    name = models.CharField(max_length=64, validators=[validate])
    class Meta:
        verbose_name = 'Справочник характеристик'
        verbose_name_plural = 'Справочник характеристик'
    def __str__(self):
        return self.name

class GuideUnitsMeasurement(models.Model):
    name = models.CharField(max_length=64, validators=[validate])
    class Meta:
        verbose_name = 'Справочник едениц измерения'
        verbose_name_plural = 'Справочник едениц измерения'
    def __str__(self):
        return self.name

class SetCharesteristicProduct(models.Model):

    GC = models.ForeignKey(GuideCharacteristic, on_delete=models.PROTECT, related_name='guidec', verbose_name='Справочник характеристик')
    GUM = models.ForeignKey(GuideUnitsMeasurement, on_delete=models.PROTECT, related_name='guideu', verbose_name='Справочник едениц измерения')
    value = models.CharField(max_length=64, validators=[validate])
    class Meta:
        verbose_name = 'Набор характеристик продукта'
        verbose_name_plural = 'Набор характеристик продукта'
    def __str__(self):
        return self.value

class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    model = models.ForeignKey(Models, on_delete=models.PROTECT, 
                                related_name='modelproduct', verbose_name='Модель')
    seasson = models.ForeignKey(Seasson, on_delete=models.PROTECT, 
                                    related_name='seassonproduct',verbose_name='Сезон')
    car_types = models.ForeignKey(CarTypes, on_delete=models.PROTECT, 
                                    related_name='cartypesproduct',verbose_name='Тип машины')
    SCP = models.ForeignKey(SetCharesteristicProduct, on_delete=models.PROTECT, 
                                    related_name='set', verbose_name='Набор характеристик продукта')
    country_manu = models.ForeignKey(CountryManufacter, on_delete=models.PROTECT, 
                                        related_name='countryproduct', verbose_name='Страна производитель',)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    image = models.ImageField(upload_to='catalog/', verbose_name='Изображение')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return "%s, %s" % (self.price, self.name)