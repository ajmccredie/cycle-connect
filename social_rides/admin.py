from django.contrib import admin
from .models import Ride, RideAttendance, RideOrganiser

# Register your models here.

admin.site.register(Ride, RideAdmin)
admin.site.register(RideOrganiser)
admin.site.register(RideAttendance)
