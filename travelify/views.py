from django.shortcuts import render
from .models import Testimony, Place, Ifem
# Create your views here.



def index(request):

    test = Testimony.objects.all()

    return render(request, "index.html", {'test': test})

def index(request):

    ifem = Ifem.objects.all()
    
    return render(request, "index.html", {'ifem': ifem})

def index(request):

    place = Place.objects.all()
    
    return render(request, "index.html", {'place': place})

