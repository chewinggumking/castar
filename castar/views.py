from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeview(request):
    page_title = "Carstar | Your Path to Stardom"
    heading = "Welcome to Castar - India's Top Casting Site"
    context = {
    "page_title":page_title,
    "heading":heading

    }
    return render(request, 'index.html', context)
