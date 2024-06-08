from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    return render(request,'homepage.html')

def allproducts(request):
    products = Product.objects.all()
    data = {
        'prodData':products
    }
    return render(request,'productpage/allproducts.html',data)


