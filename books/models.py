from enum import unique
from django.db import models

# create your models here.

class LibraryBook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100, unique=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['author']

    def __str__(self):
        return self.title
