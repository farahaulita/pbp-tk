from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=255)
    grade = models.FloatField()
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    submisson = models.FileField()