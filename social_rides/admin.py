from django.contrib import admin
from .models import Ride, RideAttendance, RideOrganiser

admin.site.register(RideAttendance)
# Admin can view and approve rides
class RideAdmin(admin.ModelAdmin):
    list_display = ('title', 'organiser', 'start_place', 'end_place', 'difficulty', 'is_verified')
    list_filter = ('difficulty', 'is_verified')
    search_fields = ('title', 'organiser__username')

    actions = ['approve_rides']

    def approve_rides(self, request, queryset):
        queryset.update(is_verified=True)
    approve_rides.short_description = "Mark selected rides as verified"
admin.site.register(Ride, RideAdmin)

# Admin can set-up 'trusted organisers' for rides
@admin.register(RideOrganiser)
class RideOrganiserAdmin(admin.ModelAdmin):
    list_display = ['user', 'trusted_organiser']
    search_fields = ['user__username']
