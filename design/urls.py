from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.design, name='design'),
    path('add/', views.add_design, name='add_design')
]