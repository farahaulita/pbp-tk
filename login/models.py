from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone

# Create your models here.
class Subject(models.Model):
    Class = models.CharField(max_length=300)
    Name = models.CharField(max_length=300)
    def __str__(self):
        return self.Name+" - "+self.Class

class User(AbstractUser):
    pass
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    subjects = models.ManyToManyField(Subject)

class Task(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.Name

class Submissions(models.Model):
    NamaMurid = models.CharField(max_length=300)
    file = models.FileField()
    date = models.DateTimeField(default=timezone.now())
    ontime = models.BooleanField(default=True)
    comment = models.TextField(default="")
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    murid = models.ForeignKey(User, on_delete=models.CASCADE)