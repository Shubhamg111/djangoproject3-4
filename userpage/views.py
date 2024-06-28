from django.shortcuts import render
from products.models import *

# Create your views here.
def homepage(request):
    products = Product.objects.filter(trending=True).order_by('-id')[:4]
    return render(request, 'home.html',{'products':products})


def showallproducts(request):
    products = Product.objects.all().order_by('-id')
    data = {
        'allproducts': products
    }
    return render(request,'products.html',data)

def productView(request,prod_id):
    product = Product.objects.get(id=prod_id)

    return render(request,'productdetails.html',{'products':product})