from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    n = len(products)
    noSlides = n//4 + ceil((n/4) - (n//4))
    context = {'noOfSlides':noSlides, 'range':range(1, noSlides) ,'products' : products}
    return render(request, 'shop/index.html', context)

def about(request):
    return render(request, 'shop/about.html')

