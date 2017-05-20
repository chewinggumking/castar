from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from .models import StarProfile, StarPhotos
# Register your models here.


class StarProfileModelAdmin(admin.ModelAdmin):
    list_display = ["user", "age", "mobile", "gender"]
    # list_filter = ["starage"]
    class Meta:
        model = StarProfile


class StarPhotosForm(forms.ModelForm):

    class Meta:
        model = StarPhotos
        fields = '__all__'
#Validator to check photos do not exceed 20 photos per user
    def clean_user(self):
        if 'user' in self.cleaned_data:
            refModel = StarPhotos.objects.filter(user=self.cleaned_data['user'])
            picCount = refModel.count()
            if picCount ==10:
                raise ValidationError ("""You have already uploaded 10 photos.
                Delete some to upload more.""")

            return self.cleaned_data['user']


class StarPhotosAdmin(admin.ModelAdmin):
    form = StarPhotosForm



admin.site.register(StarProfile, StarProfileModelAdmin)

admin.site.register(StarPhotos, StarPhotosAdmin)
#
