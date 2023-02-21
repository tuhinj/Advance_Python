from django import forms
from .models import Product

# from creation
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = [
        #     'name'
        #     'price'
        #     'details'
        # ]
        fields ="__all__"