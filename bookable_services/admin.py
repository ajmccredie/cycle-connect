# from django.contrib import admin
# from .models import Service, ServiceSlot, Booking

# # Register your models here.
# admin.site.register(Service)
# admin.site.register(ServiceSlot)
# admin.site.register(Booking)

# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price')
#     search_fields = ('name',)

# # @admin.register(Booking)
# # class BookingAdmin(admin.ModelAdmin):
# #     list_display = ['user', 'slot', 'status']
# #     list_filter = ['status']
# #     actions = ['confirm_booking']

# #     def confirm_booking(self, request, queryset):
# #         queryset.update(status='confirmed')
# #     confirm_booking.admin_note = "Mark selected bookings as confirmed"

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
        queryset.update(status='confirmed')
    verify_booking.admin_note = "Mark selected bookings as confirmed"
