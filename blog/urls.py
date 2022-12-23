# very similar to urls.py in path file 
# imported paths _ and then created a list in which they are using that path 

from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home,name='blog-home'),
    path('about/', views.about,name='blog-about'),
]

