from django.urls import path, include 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.prints, name='prints'),
    path('', views.all_products, name='products'),
    path('<print_id>', views.print_detail, name='print_detail'),
]