from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from utils.utils import *
import datetime


class Gender(models.Model):
    gender = models.CharField(max_length=150,blank=True,null=True)

class User(AbstractUser):
    phone_number = models.CharField('Телефон', max_length=127, blank=True,null=True)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE, blank=True,null=True)
    photo = models.ImageField('Фото', blank=True,upload_to='avatars/', default='avatars/user.png',null=True)
    birthdate = models.DateField('Дата рождения', default=datetime.date.today, blank=True,null=True)
    