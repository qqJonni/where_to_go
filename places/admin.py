from django.contrib import admin

from places.models import PlaceName, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ["photo_preview"]

    def photo_preview(self, obj):
        return obj.photo_preview

    photo_preview.short_description = 'Photo Preview'
    photo_preview.allow_tags = True


@admin.register(PlaceName)
class PostAdmin(admin.ModelAdmin):
    fields = ["title", "description_short", "description_long", "lat", "lon", "point_lon", "point_lat", "slug"]
    list_display = ['title']
    inlines = [ImageInline, ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['numb', 'title', 'photo_preview']
    ordering = ['numb', ]
    readonly_fields = ["photo_preview"]

    def photo_preview(self, obj):
        return obj.photo_preview

    photo_preview.short_description = 'Photo Preview'
    photo_preview.allow_tags = True
