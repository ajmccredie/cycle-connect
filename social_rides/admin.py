from django.contrib import admin
from .models import Ride, RideAttendance, RideOrganiser

# Register your models here.
class RideAdmin(admin.ModelAdmin):
    list_display = ('title', 'organiser', 'start_place', 'end_place', 'difficulty', 'is_verified')
    list_filter = ('difficulty', 'is_verified')
    search_fields = ('title', 'organiser__username')

    def approve_rides(self, request, queryset):
        queryset.update(approved=True)
    approve_rides.short_description = "Mark selected rides as verified"

admin.site.register(Ride, RideAdmin)
admin.site.register(RideOrganiser)
admin.site.register(RideAttendance)
