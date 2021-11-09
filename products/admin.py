from django.contrib import admin
from .models import Product, Department


class ProductAdmin(admin.ModelAdmin):
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
    list_display = (
        'name',
        'display_name',
    )


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Department, DepartmentAdmin)
