from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product, Department

# Create your views here.

def all_products(request):
    products = Product.objects.all()
    departments = None

    if request.GET:
        if 'department' in request.GET:
            departments = request.GET['department'].split(',')
            products = products.filter(department__name__in=departments)
            departments = Department.objects.filter(name__in=departments)

    context = {
        'products': products,
        'current_departments': departments,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
  
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

def product_detail_prints(request, product_id):
  
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail_prints.html', context)