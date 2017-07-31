from django.conf.urls import url, include
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^$', views.homeview, name = 'homepage' ),
	url(r'^list/$', views.starlist, name = 'starlist' ),
    url(r'^upload/(\d+)/$', views.uploadpics, name = 'uploadpics' ),
]
