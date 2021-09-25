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