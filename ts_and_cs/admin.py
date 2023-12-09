from django.contrib import admin
from .models import UserVerified

# Register your models here.
@admin.register(UserVerified)
class UserTermsAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'agreed_to_terms']

    def get_username(self, obj):
        return obj.user.username 
    get_username.short_description = 'Username'
