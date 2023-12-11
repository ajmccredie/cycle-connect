from django.contrib import admin
from .models import ForumPost, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(ForumPost)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'title': ('title',)}
    search_fields = ['title', 'content']
    summernote_fields = ('content')
    list_display = ('title', 'UserId', 'created_on', 'reported_status')
    list_filter = ('reported_status', 'created_on')
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(reported_status=False, published_status=1)
    make_published.short_description = "Mark selected posts as published"
    readonly_fields = ('reported_by_list',)

    def reported_by_list(self, obj):
        return ", ".join([user.username for user in obj.reported_by.all()])
    reported_by_list.short_description = 'Reported By'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('username', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


