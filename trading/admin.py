from django.contrib import admin
from .models import TradingPost, TradingConversation, Message

admin.site.register(TradingConversation)
admin.site.register(Message)


# Admin can see and approve trading posts
class TradingPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'seller', 'created_on', 'approved', 'status')
    list_filter = ('approved', 'status', 'created_on')
    search_fields = ('title', 'description', 'seller__username')
    actions = ['approve_posts', 'mark_as_sold']

    def approve_posts(self, request, queryset):
        queryset.update(approved=True)
    approve_posts.short_description = "Mark selected posts as approved"

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:  # This checks if it's a new instance
            self.message_user(request, f"New trading post '{obj.title}' has been added and is awaiting approval.", messages.INFO)

admin.site.register(TradingPost, TradingPostAdmin)