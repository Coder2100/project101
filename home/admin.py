from django.contrib import admin


from .models import Carousel, FirstFeautured, SecondFeautured, ThirdFeautured
# Register your models here.

admin.site.register(Carousel)
admin.site.register(FirstFeautured)
admin.site.register(SecondFeautured)
admin.site.register(ThirdFeautured)