from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Subject(models.Model):
    Class = models.CharField(max_length=300)
    Name = models.CharField(max_length=300)
    def __str__(self):
        return self.Name+" - "+self.Class

class User(AbstractUser):
    pass
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
    deadline = models.DateTimeField()

    def __str__(self):
        return self.Name

class Submissions(models.Model):
    NamaMurid = models.CharField(max_length=300)
    title = models.CharField(max_length=50)
    file = models.FileField()
    date = models.DateTimeField()
    ontime = models.BooleanField()

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    murid = models.ForeignKey(User, on_delete=models.CASCADE)