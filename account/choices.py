from django.db import models

GENDER = (
    ('male', 'Мужской'),
    ('female', 'Женский'),
)

class Role(models.TextChoices):
    JUSTUSER = 'JU', 'Пользователь'
    ORDERMANAGER = 'OM', 'Менеджер по заказу'
    PRODUCTMANAGER = 'PM', 'Менеджер по товару'
    OWNER = 'OW', 'Владелец'