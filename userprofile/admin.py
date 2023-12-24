from django.contrib import admin
from .models import ProfileDetails


# Allow admin full access to profiles
@admin.register(ProfileDetails)
class ProfileDetailsAdmin(admin.ModelAdmin):
    list_display =  ['user', 'biography', 'profile_picture', 'cycling_skills', 'preferred_ride_type', 'maintenance_skills']
