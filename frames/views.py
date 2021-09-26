from django.shortcuts import render, get_object_or_404
from .models import PhotoFrame

# Create your views here.

def frames(request):

    frames = PhotoFrame.objects.all()

    context = {
        'frames': frames,
    }

    return render(request, 'frames/frames.html', context)


def frame_detail(request, frame_id):

    frame = get_object_or_404(PhotoFrame, pk=frame_id)

    context = {
        'frame': frame,
    }

    return render(request, 'frames/frame_detail.html', context)