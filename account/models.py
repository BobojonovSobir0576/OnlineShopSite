from django.db import models
from django.contrib.auth.models import AbstractUser
from account.choices import GENDER
from django.urls import reverse
from utils.utils import *
import datetime


class User(AbstractUser):
    first_name = models.CharField('Фамилия', max_length=150,blank=True)
    last_name = models.CharField('Имя', max_length=150,blank=True)
    middle_name = models.CharField('Отчество', max_length=150,blank=True)
    phone_number = models.CharField('Телефон', max_length=127, blank=True,)
    gender = models.CharField('Пол', max_length=100,choices=GENDER, blank=True,)
    photo = models.ImageField('Фото', blank=True,upload_to='avatars/', default='avatars/user.png')
    birthdate = models.DateField('Дата рождения', default=datetime.date.today, blank=True)

    def get_first_order_date(self):
        return self.order_set.order_by('created_at').first().created_at
    