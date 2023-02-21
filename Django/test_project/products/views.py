from django.shortcuts import render
from .models import Product

# Create your views here.
# CRUD (Create, Retrieve/read, Update, Delete)
# CREATE
# RETRIEVE/READ
def products_list(request):
    # ORM - Object Relational Maper
    product = Product.objects.all()
    context = {
    "products": product
    }
    return render(request, 'products/product_list.html', context)

# UPDATE
# DELETE
