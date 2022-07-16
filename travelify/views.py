from django.shortcuts import render
from .models import Destination, Experience, Testimony
# Create your views here.


def index(request):

    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})

def index(request):

    exp = Experience.objects.all()
    print (exp)
    return render(request, "index.html", {'exp': exp})

def index(request):

    test = Testimony.objects.all()

    return render(request, "index.html", {'test': test})

