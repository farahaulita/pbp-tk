from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
    # name = models.BooleanField('name', default=False)
    # password = models.BooleanField('password', default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


#     def __str__(self):
#     	return self.user.username


# class Teacher(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

#     def __str__(self):
#     	return self.user.username