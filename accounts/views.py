from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def userRegister(request):
    if request.method =="POST":
        regForm = UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.add_message(request,messages.SUCCESS,"User created successfully")
            return redirect('/register/')
        else:
            messages.add_message(request,messages.ERROR,"Error in creating user")
            return render(request,'register.html',{'regForm':regForm})




    context ={
        'regForm':UserCreationForm
    }
    return render(request,'register.html',context)


def userLogin(request):
    if request.method == "POST":
        logform = LoginForm(request.POST)
        if logform.is_valid():
            data = logform.cleaned_data
            user = authenticate(username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                messages.add_message(request,messages.SUCCESS,'Login Successfull')
                return redirect('/allproducts/')
            else:
                messages.add_message(request,messages.ERROR,'Invalid Credentials')
                return render(request,'login.html',{'logForm':logform})
    context = {
        'logForm':LoginForm()
    }
    return render(request,'login.html',context)


def userlogout(request):
    logout(request)
    return redirect('/login/')