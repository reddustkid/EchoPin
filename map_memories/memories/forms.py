from django import forms
from .models import Gallery

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['user', 'name', 'gallery_images', 'gps_location', 'city', 'memories', 'date']