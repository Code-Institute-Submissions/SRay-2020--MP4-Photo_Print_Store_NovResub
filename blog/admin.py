from django.contrib import admin
from .models import Post1, Comment


@admin.register(Post1)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'status')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
