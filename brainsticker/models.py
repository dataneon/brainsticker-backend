from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    def __str__(self):
        return self.email

class Canvas(models.Model):
    # Canvas refers to its owner, User
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='canvas')
    canvas_name = models.CharField(max_length=100)

    class Meta:
        # this is for the sake of the django admin page's pluralizing the names
        verbose_name = ('Canvas')
        verbose_name_plural = ('Canvases')

    def __str__(self):
        return self.canvas_name


class Note(models.Model):
    # Note refers to its owner, Canvas
    canvas = models.ForeignKey(Canvas, on_delete=models.CASCADE, related_name='notes')
    content = models.CharField(max_length=2000)

    def __str__(self):
        return self.content
