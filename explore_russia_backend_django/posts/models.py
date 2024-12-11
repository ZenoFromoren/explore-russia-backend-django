from django.db import models
from django.core.validators import MinLengthValidator


class Post(models.Model):
    city = models.CharField(validators=[MinLengthValidator(1)], max_length=70)
    title = models.CharField(validators=[MinLengthValidator(1)], max_length=70)
    image = models.URLField()
    text = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
