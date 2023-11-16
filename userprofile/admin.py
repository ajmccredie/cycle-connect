from django.contrib import admin
from .models import ProfileDetails


@admin.register(ProfileDetails)
class ProfileDetailsAdmin(admin.ModelAdmin):
    list_display =  ['user', 'biography', 'profile_picture', 'cycling_skills', 'preferred_ride_type', 'maintenance_skills']

