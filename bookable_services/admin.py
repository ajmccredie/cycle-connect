from django.contrib import admin
from .models import Place, Booking, Slot, Service

# Register your models here.
admin.site.register(Place)
admin.site.register(Slot)
admin.site.register(Booking)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)