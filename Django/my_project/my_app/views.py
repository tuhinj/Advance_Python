from django.shortcuts import render

# Create your views here.
def home(request):
    dict ={
        'mane':'Maynuddin Tuhin Joy',
    }
    return render(request, 'home.html',dict)