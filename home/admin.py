from django.contrib import admin


from .models import Carousel, FirstFeautured, SecondFeautured, ThirdFeautured, Headline
# Register your models here.

admin.site.register(Carousel)
admin.site.register(FirstFeautured)
admin.site.register(SecondFeautured)
admin.site.register(ThirdFeautured)
admin.site.register(Headline)