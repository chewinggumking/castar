from django import forms

from .models import StarPhotos

class PhotoForm(forms.ModelForm):
    class Meta:
        model = StarPhotos
        fields = ['photos', 'category']