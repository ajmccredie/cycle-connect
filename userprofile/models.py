from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class ProfileDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True, null=True)
    profile_picture = CloudinaryField('image', default='placeholder', blank=True, null=True)
    cycling_skills = models.CharField(max_length=100, blank=True, null=True)
    preferred_ride_type = models.CharField(max_length=100, blank=True, null=True)
    maintenance_skills = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.user.username

