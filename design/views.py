from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

# Create your views here.

def add_design(request):

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully Added your design.')
            return redirect(reverse('product_detail', args=[product.id]))

        else:
            messages.error(request, 'Failed to add design, please ensure form is valid.')
            
    else:
        form = ProductForm()

    template = 'design/add_design.html'
    context = {
        'form': form,
    }


    return render(request, template, context)