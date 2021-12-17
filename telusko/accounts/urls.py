from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name ='login'),
    path('logout', views.logout, name = 'logout'),
    path('destinations', views.destinations, name = 'destinations'),
    path('news', views.news, name = 'news'),
    path('contact.html', views.contact, name = 'contact'),
    path('index.html', views.index),     # index.html comes from registration.html button
]