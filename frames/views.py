from django.shortcuts import render
from .models import PhotoFrame

# Create your views here.

def frames(request):

    frames = PhotoFrame.objects.all()

    context = {
        'frames': frames,
    }

    return render(request, 'frames/frames.html', context)