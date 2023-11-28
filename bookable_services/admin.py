from django.contrib import admin
from .models import Place, Booking, Slot

# Register your models here.
admin.site.register(Place)
admin.site.register(Slot)
admin.site.register(Booking)