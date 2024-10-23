from django.db import models

class Question(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200,default=0)
    