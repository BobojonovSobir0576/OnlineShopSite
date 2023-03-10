# Generated by Django 4.1.6 on 2023-02-08 17:45

from django.db import migrations, models
import django.db.models.deletion
import utils.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, validators=[utils.utils.validate])),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.CreateModel(
            name='CarTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64, validators=[utils.utils.validate])),
            ],
            options={
                'verbose_name': 'Тип машины',
                'verbose_name_plural': 'Типы Машин',
            },
        ),
        migrations.CreateModel(
            name='CountryManufacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, validators=[utils.utils.validate])),
            ],
            options={
                'verbose_name': 'Страны производителей',
                'verbose_name_plural': 'Страна производителя',
            },
        ),
        migrations.CreateModel(
            name='GuideCharacteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, validators=[utils.utils.validate])),
            ],
            options={
                'verbose_name': 'Справочник характеристик',
                'verbose_name_plural': 'Справочник характеристик',
            },
        ),
        migrations.CreateModel(
            name='GuideUnitsMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, validators=[utils.utils.validate])),
            ],
            options={
                'verbose_name': 'Справочник едениц измерения',
                'verbose_name_plural': 'Справочник едениц измерения',
            },
        ),
        migrations.CreateModel(
            name='Models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, validators=[utils.utils.validate])),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='brandmodel', to='catalog.brands', verbose_name='Бренд')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модель',
            },
        ),
        migrations.CreateModel(
            name='Seasson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seasson', models.CharField(max_length=64, validators=[utils.utils.validate])),
            ],
            options={
                'verbose_name': 'Сезон',
                'verbose_name_plural': 'Сезоны',
            },
        ),
        migrations.CreateModel(
            name='SetCharesteristicProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=64, validators=[utils.utils.validate])),
                ('GC', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='guidec', to='catalog.guidecharacteristic', verbose_name='Справочник характеристик')),
                ('GUM', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='guideu', to='catalog.guideunitsmeasurement', verbose_name='Справочник едениц измерения')),
            ],
            options={
                'verbose_name': 'Набор характеристик продукта',
                'verbose_name_plural': 'Набор характеристик продукта',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=64, null=True, validators=[utils.utils.validate])),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('description', models.TextField(blank=True, default=None, null=True, validators=[utils.utils.validate])),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='catalog/', verbose_name='Изображение')),
                ('slug', models.SlugField(unique=True)),
                ('SCP', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='set', to='catalog.setcharesteristicproduct', verbose_name='Набор характеристик продукта')),
                ('car_types', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cartypesproduct', to='catalog.cartypes', verbose_name='Тип машины')),
                ('country_manu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='countryproduct', to='catalog.countrymanufacter', verbose_name='Страна производитель')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='modelproduct', to='catalog.models', verbose_name='Модель')),
                ('seasson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='seassonproduct', to='catalog.seasson', verbose_name='Сезон')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
