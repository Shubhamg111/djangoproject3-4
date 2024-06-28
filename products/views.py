from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def allProducts(request):
    products = Product.objects.all()
    data = {
        'prodData':products
    }
    return render(request,'productpage/allproducts.html',data)


def addCategory(request):
    if request.method=="POST":
        catForm = CategoryForm(request.POST)
        if catForm.is_valid():
            catForm.save()
            messages.add_message(request,messages.SUCCESS,'Category Added')
            return redirect('/addcategory/')
        else:
            messages.add_message(request,messages.ERROR,'Category Not Added')
            return render(request,'productpage/addcategory.html',{'catForm' : catForm})

    catForm=CategoryForm()
    # context={
    #     'catForm' : catForm
    # }
    
    return render(request,'productpage/addcategory.html',{'catForm' : catForm})


def addProduct(request):
    if request.method=="POST":
        prodForm = ProductForm(request.POST,request.FILES)
        if prodForm.is_valid():
            prodForm.save()
            messages.add_message(request,messages.SUCCESS,'Product Added')
            return redirect('/addproducts/')
        else:
            messages.add_message(request,messages.ERROR,'Product Not Added')
            return render(request,'productpage/addproduct.html',{'prodForm' : prodForm})

    prodForm=ProductForm()
    return render(request,'productpage/addproduct.html',{'prodForm':prodForm})



def allCategory(request):
    category = Category.objects.all()
    data = {
        'category':category
    }
    return render(request,'productpage/allcategory.html',data)


def deleteCategory(request,category_id):
    category=Category.objects.get(id = category_id)
    category.delete()
    messages.add_message(request,messages.SUCCESS,'Categroy Deleted.')
    return redirect('/allcategory/')
    

def updateCategory(request,category_id):
    instance=Category.objects.get(id = category_id)

    if request.method=='POST':
        catForm = CategoryForm(request.POST,instance=instance)
        if catForm.is_valid():
            catForm.save()
            messages.add_message(request,messages.SUCCESS,'Item Updated')
            return redirect('/allcategory/')
        else:
            messages.add_message(request,messages.ERROR,'Somthing Went Wrong')
            return render(request,'productpage/updatecategory.html',{'catForm' : catForm})
    data ={
        'catForm':CategoryForm(instance=instance)
    }
    return render(request,'productpage/updatecatgory.html',data)


def deleteProduct(request,product_id):
    product=Product.objects.get(id = product_id)
    product.delete()
    messages.add_message(request,messages.SUCCESS,'Product Deleted.')
    return redirect('/allproducts/')
    


def updateProduct(request,product_id):
    instance=Product.objects.get(id = product_id)

    if request.method=='POST':
        prodForm = ProductForm(request.POST,request.FILES,instance=instance)
        if prodForm.is_valid():
            prodForm.save()
            messages.add_message(request,messages.SUCCESS,'Item Updated')
            return redirect('/allproducts/')
        else:
            messages.add_message(request,messages.ERROR,'Somthing Went Wrong')
            return render(request,'productpage/updateproduct.html',{'prodForm' : prodForm})
    data ={
        'prodForm':ProductForm(instance=instance)
    }
    return render(request,'productpage/updateproduct.html',data)

