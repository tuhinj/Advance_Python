from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class HomepageView(View):
    def get(self,request, *args, **kwargs):
        return render(request,'ads/index.html')


# class AdListView(ListView):
#     pass