from django.contrib import admin
from .models import Product, Department

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'department',
        'price',
        'description',
        'image',
    )

    ordering = ('sku',)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Department, DepartmentAdmin)