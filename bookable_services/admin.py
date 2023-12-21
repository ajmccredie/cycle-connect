from django.contrib import admin
from .models import Place, Booking, Slot, Service
from django.contrib import messages

# Register your models here.
admin.site.register(Place)
admin.site.register(Slot)

# Admin can view and add services to the system
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

# Admin can view and approve service bookings
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'slot', 'status']
    list_filter = ['status']
    actions = ['confirm_booking']
    # Make admin actions easier to handle bookings
    def verify_booking(self, request, queryset):
        queryset.update(status='confirmed')
        confirm_booking.admin_note = "Mark selected bookings as confirmed"
    # Alert to admin within the Booking section of the admin panel
    def changelist_view(self, request, extra_context=None):
        new_bookings = Booking.objects.filter(status='pending')
        if new_bookings.exists():
            message = f"There are {new_bookings.count()} new bookings."
            messages.warning(request, message)
        return super().changelist_view(request, extra_context)
