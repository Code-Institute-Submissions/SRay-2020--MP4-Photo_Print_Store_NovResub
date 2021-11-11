""" This defines the admin settings and their order for the Blog app"""
from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ This class defines what value pairs are featured
    on the posts section of the blog admin """
    list_display = ('title', 'author', 'created_on', 'status')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ This class defines what value pairs are featured
    on the comments section of the blog admin """
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """ This sets approval values for comments in blog """
        queryset.update(active=True)
