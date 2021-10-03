from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

from .models import Product, Department
from .forms import ProductForm

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

def all_prints(request):
    prints = Product.objects.filter(department="1")
    
    context = {
        'prints': prints,
    }

    return render(request, 'products/prints.html', context)


def all_frames(request):
    frames = Product.objects.filter(department="2")
    
    context = {
        'frames': frames,
    }

    return render(request, 'products/frames.html', context)



def product_detail(request, product_id):
  
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def product_detail_prints(request, product_id):
  
    prints = Product.objects.filter(department="1")
    
    context = {
        'prints': prints,
    }

    return render(request, 'products/product_detail_prints.html', context)



@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'This feature is for Admin only.')
        return redirect(reverse('home'))


    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully Added new product.')
            return redirect(reverse('product_detail', args=[product.id]))

        else:
            messages.error(request, 'Failed to add product, please ensure form is valid.')
            
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }


    return render(request, template, context)


@login_required
def edit_product(request, product_id):

    if not request.user.is_superuser:
        messages.error(request, 'This feature is for Admin only.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product, please ensure form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing { product.name }')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    
    if not request.user.is_superuser:
        messages.error(request, 'This feature is for Admin only.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product Deleted')
    return redirect(reverse('home'))