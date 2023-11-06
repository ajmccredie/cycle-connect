from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class ProfileDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True)
    profile_picture = CloudinaryField('image', default='placeholder')
    cycling_skills = models.CharField(max_length=100, blank=True)
    preferred_ride_type = models.CharField(max_length=100, blank=True)
    maintenance_skills = models.CharField(max_length=100, blank=True)

