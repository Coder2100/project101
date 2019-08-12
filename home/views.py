from django.shortcuts import render
from django.http import Http404

from .models import *
# Create your views here.

def index(request):
    #semi_headline = Headline.objects.order_by('content')[0:100].get()
    context = {
        'slides': Carousel.objects.all(),
        'firsts': FirstFeautured.objects.all().order_by('-id')[:1],
        'seconds': SecondFeautured.objects.all().order_by('-id')[:1],
        'thirds': ThirdFeautured.objects.all().order_by('-id')[:1],
        'headlines': Headline.objects.all().order_by('-id')[:3]
    }

    return render(request, 'home/index.html', context)


def headline(request, headline_id):
    try:
        headline = Headline.objects.get(pk=headline_id)
    except Headline.DoesNotExist:
    #except Headline.DoesNotExist:
        raise Http404("The Headline does not exist")
        context = {
            "headline":Headline.objects.all()
        }
    return render(request, "home/headline.html", context)