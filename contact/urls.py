from django.urls import path, include

#import views
from  contact import views

#import contact view
from  .views import contact, answer

app_name = 'contact'

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('answer', views.answer, name='answer'),
]