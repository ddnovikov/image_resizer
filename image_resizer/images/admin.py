from django.contrib import admin

from .models import Image


class ImageAdmin(admin.ModelAdmin):
    class Meta:
        model = Image

admin.site.register(Image, ImageAdmin)
