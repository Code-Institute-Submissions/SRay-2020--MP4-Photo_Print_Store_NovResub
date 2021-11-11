""" This is the configuration for Products app"""
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """ This configures the Products app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
