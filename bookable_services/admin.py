from django.contrib import admin
from .models import Place, Booking, Slot, Service

# Register your models here.
admin.site.register(Place)
admin.site.register(Slot)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'slot', 'status']
    list_filter = ['status']
    actions = ['verify_booking']

    def verify_booking(self, request, queryset):
        queryset.update(status='verified')
    verify_booking.admin_note = "Mark selected bookings as verified"