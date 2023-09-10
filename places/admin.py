from django.contrib import admin
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin

from places.models import PlaceName, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ["preview_photo"]

    def preview_photo(self, obj):
        return obj.preview_photo

    preview_photo.short_description = 'Preview Photo'
    preview_photo.allow_tags = True


@admin.register(PlaceName)
class PostAdmin(SortableAdminBase, admin.ModelAdmin):
    fields = ["title", "short_description", "long_description", "longitude", "latitude"]
    list_display = ['pk', 'title']
    inlines = [ImageInline, ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    def preview_photo(self, obj):
        return obj.photo_preview

    preview_photo.short_description = 'Preview Photo'
    preview_photo.allow_tags = True
