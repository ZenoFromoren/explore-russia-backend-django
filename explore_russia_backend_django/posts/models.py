from django.db import models
from django.core.validators import MinLengthValidator
from itertools import chain


class Post(models.Model):
    city = models.CharField(validators=[MinLengthValidator(1)], max_length=70)
    title = models.CharField(validators=[MinLengthValidator(1)], max_length=70)
    image = models.URLField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_dict(instance):
        opts = instance._meta
        data = {}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = f.value_from_object(instance)
        for f in opts.many_to_many:
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"
