from django.shortcuts import render
from .models import Destinations

# Create your views here.
def index(request):
    dests = Destinations.objects.all()
    return render(request, 'index.html', {'dests':dests})

def about(request):
    return render(request, 'about.html')

def news(request):
    return render(request, 'news.html')

def contact(request):
    return render(request, 'contact.html')

def destinations(request):
    return render(request, 'destinations.html')

def elements(request):
    return render(request, 'elements.html')

def login(request):
    return render(request, 'login.html')

def destinations(request):
    dests = Destinations.objects.all()
    if User is None:
        return render(request, 'destinations.html', {'dests':dests})
    else:
        return redirect('/')

def news(request):
    if User is None:
        return render(request, 'news.html')
    else:
        return redirect('/')
