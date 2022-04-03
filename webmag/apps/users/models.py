from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from ..users.managers import UserManager

class User(AbstractUser, PermissionsMixin):

    username = models.CharField(max_length=100, unique=True, verbose_name='Пользователь')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    password = models.CharField(max_length=225)
    image = models.ImageField(verbose_name='Фото пользователя')
    resume = models.TextField(max_length=500, verbose_name='Краткое резюме автора')

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Все пользователи'

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Staff(User):

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

