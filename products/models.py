""" This defines the models used for the products app """
from django.db import models

# Create your models here.


class Department(models.Model):
    """ This contains the parameters for the department class """
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        """ This returns the name that will be displayed to the user """
        return self.display_name


class Product(models.Model):
    """ This contains the parameters for the product class """
    department = models.ForeignKey(
        'Department', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    dimensions = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.name
