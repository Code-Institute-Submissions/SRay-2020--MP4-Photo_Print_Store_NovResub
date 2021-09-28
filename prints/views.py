from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def prints(request):

    prints = PhotoPrint.objects.all()

    context = {
        'prints': prints,
    }

    return render(request, 'prints/prints.html', context)


def print_detail(request, print_id):

    print = get_object_or_404(PhotoPrint, pk=print_id)

    context = {
        'print': print,
    }

    return render(request, 'prints/print_detail.html', context)


def all_products(request):
    products = Products.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)