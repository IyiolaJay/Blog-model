from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField
    author = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING,)
    created_date = models.DateTimeField
    Published_date = models.DateTimeField

    def __str__(self) -> str:
        return f'author: {self.author}'
        