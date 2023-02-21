from django.shortcuts import render
from .models import Product
from .forms import ProductForm


# Create your views here.
# CRUD (Create, Retrieve/read, update, delete)
# Retieve / read
def product_list(request):
    # ORM - Object Relational Mapper
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/products_list.html',context)

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'pro_d': product
    }
    return render(request, 'products/products_detail.html', context)

# Create:
def create_product(request):
    form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/products_form.html', context)