from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.urls import reverse

from .models import StarProfile, StarPhotos
from .forms import PhotoForm


# Create your views here.
@login_required
def homeview(request,):
	if request.user.is_staff == False:
		star = get_object_or_404(StarProfile, user=request.user)
	else:
		star = None
	if star:
		pics = StarPhotos.objects.filter(user=star.user)
	else:
		pics = None
	page_title = "Your Path to Stardom"
	heading = "Welcome to Castar - India's Top Casting Site"
	print (request.user)
	context = {
	"page_title":page_title,
	"heading":heading,
	"star":star,
	"pics":pics,
	}
	return render(request, 'index.html', context)


def starlist(request):
	users = User.objects.filter(is_staff=False)
	page_title = "List of Stars"
	context = {
		"page_title" : page_title,
		"users" : users,
	}
	return render(request, 'list.html', context)

@login_required
def uploadpics(request, userid):
	starpics = StarPhotos.objects.filter(user=int(userid))
	form = PhotoForm()
	context = {
		"pics": starpics,
		"title": "Upload Your Pics here",
		"form" : form,
		"noPics": starpics.count()
	}
	return render(request, "uploadform.html", context)