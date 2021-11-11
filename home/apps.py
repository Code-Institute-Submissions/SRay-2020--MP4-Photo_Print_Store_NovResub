""" This is the configuration for home application """
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """ This contains the configuration for Home app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
