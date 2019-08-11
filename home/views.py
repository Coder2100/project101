from django.shortcuts import render
from .models import Carousel
# Create your views here.

def index(request):
  
    context = {
        'slides': Carousel.objects.all()
    }

    return render(request, 'home/index.html', context)