from django.shortcuts import render, redirect
import requests
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def index(request):
    blogdetails = blog.objects.all()
    print(blogdetails.values())
    return render(request,'index.html',{'blog':blogdetails})

def userBlog(request):
    blogdetails = blog.objects.all()
    print(blogdetails.values())
    return render(request,'user_blog.html',{'blog':blogdetails})

def updateBlog(request,id):
    return render(request,'update_blog.html')

def deleteBlog(request,id):
    return render(request,'index.html')

def register(request):
    c={}
    if request.method == "POST":
        fname=request.POST.get('firstName')
        lname=request.POST.get('lastName')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if not User.objects.filter(email=email).exists():
            user_details=User(first_name=fname,last_name=lname,email=email,username=email)    
            user_details.set_password(password)
            user_details.save()
            return render(request,'index.html')
        else:
            c={'error':'Email Exist','fname':fname,'lname':lname,'email':email,'password':password}
            return render(request,'register.html',c)
    return render(request,'register.html')

def login(request):
    c={}
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user and user.is_active:
            auth_login(request, user)
            print(user.username)
            return redirect('webapp:index')
        else:
            c={'error':'Invalid Email or Password. Please try again.'}
    return render(request,'login.html',c)

def logout(request):
    auth_logout(request)
    return index(request)