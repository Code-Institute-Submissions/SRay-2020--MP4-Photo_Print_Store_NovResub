from django.db import models

# Create your models here.

class PhotoPrint(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    department = models.ForeignKey('Department', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    dimensions = models.CharField(max_length=254)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.name



# admin.py PhotoPrints 

from django.contrib import admin
from .models import PhotoPrint

# Register your models here.

class PrintAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'sku',
        'price',
        'image',
    )

    ordering = ('sku',)


admin.site.register(PhotoPrint, PrintAdmin)


# From prints views.py 

from .models import PhotoPrint, Product

def prints(request):

    prints = PhotoPrint.objects.all()

    context = {
        'prints': prints,
    }

    return render(request, 'prints/prints.html', context)