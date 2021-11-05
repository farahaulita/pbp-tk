from django.db import models

# Create your models here.
<<<<<<< HEAD

=======
class Suggestion(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField(max_length=200)
>>>>>>> 895d920d906c78739bbed892074bd829788cf032
