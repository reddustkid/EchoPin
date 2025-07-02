from django.contrib import admin
from .models import Gallery
admin.site.site_header = "EchoPin Management"
admin.site.site_title = "EchoPin Admin Portal"
admin.site.index_title = "Welcome to EchoPin Dashboard"


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "gallery_images", "gps_location", "city")
    search_fields = ("user", "name", "gallery_images", "gps_location", "city")
    list_filter = ("user", "name", "gallery_images", "gps_location", "city")