from django.shortcuts import render, redirect
import requests
from .models import *

# Create your views here.
def index(request):
    blogdetails = blog.objects.all()
    print(blogdetails.values())
    return render(request,'index.html',{'blog':blogdetails})


def update(request):
    return render(request,'update.html')