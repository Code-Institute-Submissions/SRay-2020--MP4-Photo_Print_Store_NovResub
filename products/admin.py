""" This defines the admin settings and their order for the Products app"""
from django.contrib import admin
from .models import Product, Department


class ProductAdmin(admin.ModelAdmin):
    """ This class defines what value pairs are featured
    on the products admin """
    list_display = (
        'name',
        'description',
        'dimensions',
        'sku',
        'price',
        'image',
    )

    ordering = ('name',)


class DepartmentAdmin(admin.ModelAdmin):
    """ This class defines what value pairs
    are featured on the departments admin """
    list_display = (
        'name',
        'display_name',
    )


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Department, DepartmentAdmin)
