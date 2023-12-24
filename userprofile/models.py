from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Data model for profile details
class ProfileDetails(models.Model):
    #Fields added to fix rendering issue in template
    CYCLING_SKILLS_CHOICES = [
        ('beginner', 'Beginner'),
        ('casual', 'Casual'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    PREFERRED_RIDE_TYPE_CHOICES = [
    ("road", "Road"),
    ("electric", "Electric"),
    ("bmx", "BMX"),
    ("mountain", "Mountain"),
    ("hybrid", "Hybrid"),
    ]

    MAINTENANCE_SKILLS_CHOICES = [
        ('none', 'None'),
        ('casual', 'Casual'),
        ('basic', 'Basic'),
        ('advanced', 'Advanced'),
        ('youtube_is_my_hero', 'YouTube is my hero!'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True, null=True)
    profile_picture = CloudinaryField('image', default='placeholder', blank=True, null=True)
    cycling_skills = models.CharField(max_length=100, blank=True, null=True, choices=CYCLING_SKILLS_CHOICES)
    preferred_ride_type = models.CharField(max_length=100, blank=True, null=True, choices=PREFERRED_RIDE_TYPE_CHOICES)
    maintenance_skills = models.CharField(max_length=100, blank=True, null=True, choices=MAINTENANCE_SKILLS_CHOICES)

    def __str__(self):
        return self.user.username

    def get_cycling_skills_display(self):
        return dict(self.CYCLING_SKILLS_CHOICES).get(self.cycling_skills, '')

    def get_preferred_ride_type_display(self):
        return dict(self.PREFERRED_RIDE_TYPE_CHOICES).get(self.preferred_ride_type, '')

    def get_maintenance_skills_display(self):
        return dict(self.MAINTENANCE_SKILLS_CHOICES).get(self.maintenance_skills, '')


# Data model for use notifications (un-used within project scope)
class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.recipient.username}: {self.message}"
