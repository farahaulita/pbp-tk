from django.db import models
from login.models import User #add this
from django.dispatch import receiver #add this
from django.db.models.signals import post_save
from datetime import datetime
# SOURCE: https://www.ordinarycoders.com/django-custom-user-profile

class Profile(models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'undraw_profile.svg', upload_to='profile_pics')
    name = models.CharField(max_length=256, default="Enter Name")
    birth_date = models.DateField(default=datetime.now)
    address = models.CharField(max_length=256, default="Enter Address")
	
    

    @receiver(post_save, sender=User) #add profile if user is created
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
 
    @receiver(post_save, sender=User) #save profile if user is saved
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

