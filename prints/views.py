from django.shortcuts import render
from .models import PhotoPrint

# Create your views here.

def prints(request):

    prints = PhotoPrint.objects.all()

    context = {
        'prints': prints,
    }

    return render(request, 'prints/prints.html', context)