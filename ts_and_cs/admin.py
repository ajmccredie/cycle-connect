from django.contrib import admin
from .models import UserVerified

# Register your models here.
@admin.register(UserVerified)
class UserTermsAdmin(admin.ModelAdmin):
    list_display = ['username', 'agreed_to_terms']