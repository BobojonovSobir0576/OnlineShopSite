from django.db import models
from catalog.models import Product
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from profiles.models import *

User = get_user_model()


class OrderStatus(models.IntegerChoices):
    NOT_DONE = 0, 'Не выполнено'
    DONE = 1, 'Выполнено'
    CANCELED = 2, 'Отменено'

class Pay(models.TextChoices):
    CASH = 'CH', 'Наличные'
    CREDIT_CARD = 'CC', 'Кредитная карта'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.PROTECT, blank=True, null=True, default=None, verbose_name='Покупатель')
    manager_order = models.ForeignKey(Staff, on_delete=models.CASCADE,verbose_name='Менеджер по формлению заказа')
    payment = models.CharField('Способ оплаты', max_length=2,
                              choices=Pay.choices, blank=True)
    product = models.ForeignKey(Product, on_delete = models.PROTECT, blank=True, null=True, default=None, verbose_name='Товар')
    
    nmb = models.IntegerField('Количетво товаров', default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#total price for all products in order

    status = models.IntegerField(verbose_name='Состояние', choices=OrderStatus.choices, default=0)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return f'Заказ {self.id, self.status}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        print (self.nmb)

        self.total_price = int(self.nmb) * price_per_item

        super(Order, self).save(*args, **kwargs)