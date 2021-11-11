""" This file contains the views displayed in the home app """
from django.shortcuts import render

# Create your views here.


def index(request):
    """ This renders the index.html/home page of app """
    return render(request, 'home/index.html')
