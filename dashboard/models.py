from django.db import models
from login.models import User #add this
from django.dispatch import receiver #add this
from django.db.models.signals import post_save
from datetime import date
# SOURCE: https://www.ordinarycoders.com/django-custom-user-profile

class Profile(models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    name = models.CharField(max_length=256, default="Name")
    birth_date = models.DateField(default=date.today())
    address = models.CharField(max_length=256, default="Name")
	
    def __str__(self):
        return User
=======
    image = models.ImageField(default = 'undraw_profile.svg', upload_to='profile_pics')
    name = models.CharField(max_length=256, default="Enter Name")
    birth_date = models.DateField(default=date.today())
    address = models.CharField(max_length=256, default="Enter Address")
	
    
>>>>>>> 895d920d906c78739bbed892074bd829788cf032

    @receiver(post_save, sender=User) #add profile if user is created
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
<<<<<<< HEAD

=======
 
>>>>>>> 895d920d906c78739bbed892074bd829788cf032
    @receiver(post_save, sender=User) #save profile if user is saved
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

