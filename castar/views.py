from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import StarProfile, StarPhotos
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.
@login_required
def homeview(request,):
    star = get_object_or_404(StarProfile, user=request.user)
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


# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect (reverse('homepage'))
