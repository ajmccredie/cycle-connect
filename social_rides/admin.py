from django.contrib import admin
from .models import Ride, RideAttendance, RideOrganiser

# Register your models here.
class RideAdmin(admin.ModelAdmin):
    list_display = ('title', 'organiser', 'start_place', 'end_place', 'difficulty', 'is_verified')
    list_filter = ('difficulty', 'is_verified')
    search_fields = ('title', 'organiser__username')

admin.site.register(Ride, RideAdmin)
admin.site.register(RideOrganiser)
admin.site.register(RideAttendance)
