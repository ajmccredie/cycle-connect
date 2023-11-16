from django.contrib import admin
from .models import ForumPost, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(ForumPost)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'title': ('title',)}
   # list_filter = ('created_on')
   # list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('username', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


