from django.urls import path

from .views import index, headline
from .import views 
app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path("<int:headline_id>", views.headline, name="headline"),
    #path('<int:headline_id>', views.headline, name='headline')
]

