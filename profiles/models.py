from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class AbstractProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE
    )
    
    class Meta:
        abstract = True

class Staff(AbstractProfile):

    def __str__(self) -> str:
        return f'{self.user}'
    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'