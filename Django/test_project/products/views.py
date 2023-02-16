from django.shortcuts import render

# Create your views here.
# CRUD (Create, Retrieve/read, Update, Delete)
# CREATE
# RETRIEVE/READ
def product_list(request):
    return render(request, 'products/product_list.html')


# UPDATE
# DELETE
