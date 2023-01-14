from django.contrib import admin
from django.utils.html import format_html

from .models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    readonly_fields = ['headshot_image']
    
    def headshot_image(self, obj):
        return format_html('<img src="{url}" height="200px" />'.format(
            url = obj.image.url)
    )

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline,]
