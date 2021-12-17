from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('about', views.about),
    path('news', views.news),
    path('contact', views.contact),
    path('destinations', views.destinations),
    path('elements', views.elements),


]