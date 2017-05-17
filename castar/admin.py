from django.contrib import admin
from .models import StarProfile, StarPhotos
# Register your models here.


class StarProfileModelAdmin(admin.ModelAdmin):
    list_display = ["user", "age", "mobile", "gender"]
    # list_filter = ["starage"]
    class Meta:
        model = StarProfile


admin.site.register(StarProfile, StarProfileModelAdmin)

admin.site.register(StarPhotos)
