from django.db import models

# Create your models here.
class Blog_user(models.Model):
    author = models.CharField(max_length=50)


    def __str__(self) -> str:
        return f'{self.author}'


class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField
    Author = models.ForeignKey('Author', on_delete=models.DO_NOTHING,)
    created_date = models.DateTimeField
    Published_date = models.DateTimeField

    def __str__(self) -> str:
        return f'author: {self.Author}'