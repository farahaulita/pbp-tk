from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class Subject(models.Model):
    Class = models.CharField(max_length=300)
    Name = models.CharField(max_length=300)
    def __str__(self):
        return (str(self.Name) if self.Name else '') + " - " + (str(self.Class) if self.Class else '')

class User(AbstractUser):
    # name = models.BooleanField('name', default=False)
    # password = models.BooleanField('password', default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    subjects = models.ManyToManyField(Subject)


# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


#     def __str__(self):
#     	return self.user.username


# class Teacher(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

#     def __str__(self):
#     	return self.user.username


class Task(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField(max_length=300)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    deadline = models.DateTimeField(default=datetime.now)
    score = models.IntegerField()

    def __str__(self):
        return (str(self.Name) if self.Name else '')

class Submissions(models.Model):
    NamaMurid = models.CharField(max_length=300)
    title = models.CharField(max_length=50)
    file = models.FileField()
    date = models.DateTimeField(default=datetime.now)
    ontime = models.BooleanField()
    comment = models.TextField(default="")
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    murid = models.ForeignKey(User, on_delete=models.CASCADE)
    nilai = models.IntegerField()