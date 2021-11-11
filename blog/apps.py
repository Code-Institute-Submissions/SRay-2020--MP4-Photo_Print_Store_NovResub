""" This is the configuration for blog app"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """ This configures the blog app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
