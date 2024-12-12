from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    city = models.CharField(max_length=70)
    about = models.TextField(max_length=255)
    avatar = models.ImageField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
