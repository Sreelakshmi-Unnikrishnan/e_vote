from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=100)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)