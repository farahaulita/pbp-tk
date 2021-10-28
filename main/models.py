from django.db import models

# Create your models here.
class Suggestion(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField(max_length=200)