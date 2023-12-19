from django.contrib import admin
from .models import Ride, RideAttendance, RideOrganiser

# Register your models here.

admin.site.register(RideAttendance)

class RideAdmin(admin.ModelAdmin):
    list_display = ('title', 'organiser', 'start_place', 'end_place', 'difficulty', 'is_verified')
    list_filter = ('difficulty', 'is_verified')
    search_fields = ('title', 'organiser__username')

    actions = ['approve_rides']

    def approve_rides(self, request, queryset):
        queryset.update(approved=True)
    approve_rides.short_description = "Mark selected rides as verified"
admin.site.register(Ride, RideAdmin)

@admin.register(RideOrganiser)
class RideOrganiserAdmin(admin.ModelAdmin):
    list_display = ['user', 'trusted_organiser']
    search_fields = ['user__username']
