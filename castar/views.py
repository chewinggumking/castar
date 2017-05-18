from django.shortcuts import render
from django.http import HttpResponse
from .models import StarProfile, StarPhotos
from django.contrib.auth.models import User

# Create your views here.
def homeview(request,):
    star = StarProfile.objects.get(id=1)
    pics = StarPhotos.objects.filter(user=star.user)
    page_title = "Carstar | Your Path to Stardom"
    heading = "Welcome to Castar - India's Top Casting Site"
    print (request.user)
    context = {
    "page_title":page_title,
    "heading":heading,
    "star":star,
    "pics":pics,
    }
    return render(request, 'index.html', context)
