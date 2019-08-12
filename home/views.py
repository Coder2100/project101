from django.shortcuts import render
from .models import Carousel, FirstFeautured, SecondFeautured, ThirdFeautured
# Create your views here.

def index(request):
  
    context = {
        'slides': Carousel.objects.all(),
        'firsts': FirstFeautured.objects.all(),
        'seconds': SecondFeautured.objects.all(),
        'thirds': ThirdFeautured.objects.all()
    }

    return render(request, 'home/index.html', context)