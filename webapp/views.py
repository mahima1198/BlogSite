from django.shortcuts import render, redirect
import requests
from .models import *

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
    return render(request,'register.html')