from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    city = models.CharField(
        max_length=70, blank=True, null=True, default="Город не указан"
    )
    about = models.TextField(
        max_length=255, blank=True, null=True, default="Пока ничего не рассказал о себе"
    )
    avatar = models.CharField(null=True)

    REQUIRED_FIELDS = ("password", )

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.username

    class Meta:
        db_table = "Users"
        verbose_name = "User"
        verbose_name_plural = "Users"
