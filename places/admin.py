from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableTabularInline

from .models import Place, PlaceImage


class PlaceImageTabularInline(SortableTabularInline):
    model = PlaceImage
    readonly_fields = ['headshot_image']
    ordering = ['order',]
    
    def headshot_image(self, obj):
        return format_html(
            '<img src="{}" style="max-height: 200px; max-width: 400px" />',
            obj.image.url
        )

@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [PlaceImageTabularInline,]
    search_fields = ['title',]
