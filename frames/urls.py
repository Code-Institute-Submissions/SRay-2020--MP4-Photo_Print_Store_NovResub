from django.urls import path, include 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.frames, name='frames'),
    path('<frame_id>', views.frame_detail, name='frame_detail'),
] 

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
