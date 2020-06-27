from django.contrib import admin 
from django.urls import path, include 
from . import views
urlpatterns = [ 
    path('', views.atencion), 
    # Enter the app name in following 
    # syntax for this to work 
  
] 