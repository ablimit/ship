from django.db import models

# Create your models here.

class Question(models.Model):
    text   = models.CharField(max_length=30000)
    answer = models.CharField(max_length=30000)
    category = models.CharField(max_length=30000)


