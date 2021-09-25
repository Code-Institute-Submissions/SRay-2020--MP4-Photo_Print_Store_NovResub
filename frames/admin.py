from django.contrib import admin
from .models import PhotoFrame

# Register your models here.

class FrameAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'dimensions',
        'sku',
        'price',
        'image',
    )

    ordering = ('name',)

admin.site.register(PhotoFrame, FrameAdmin)