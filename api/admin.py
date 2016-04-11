from django.contrib import admin
from django.utils.html import format_html

from .models import Media


class MediaAdmin(admin.ModelAdmin):
    list_display = ("display", "thumbnail")

    def display(self, media_obj):
        return format_html(
            '<a href="%s">%s</a>' % (media_obj.file.url, media_obj.file.name)
        )

    def thumbnail(self, media_obj):
        location = media_obj.file.url
        thumbnail_html = "<a href=\"{0}\"><img border=\"0\" alt=\"\" src=\"{1}\" height=\"80\" /></a>".format(location, location)
        return format_html(thumbnail_html)

admin.site.register(Media, MediaAdmin)
