from django.db import models
from django.contrib.auth.models import User #add this
from django.dispatch import receiver #add this
from django.db.models.signals import post_save
# SOURCE: https://www.ordinarycoders.com/django-custom-user-profile


"""class Profile(models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    birth_date = models.DateField()
    address = models.CharField(max_length=256)
	

    @receiver(post_save, sender=User) #add profile if user is created
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User) #save profile if user is saved
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
"""

# User profile here
