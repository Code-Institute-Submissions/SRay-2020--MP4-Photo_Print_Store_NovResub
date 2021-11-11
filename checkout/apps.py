""" This is the configuration for the checkout app"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ This class sets the config for the checkout feature """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
