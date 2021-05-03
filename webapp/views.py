from django.shortcuts import render, redirect, get_object_or_404
import requests
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
def index(request):
    blogdetails = blog.objects.all().reverse()[:5]
    return render(request,'index.html',{'blog':blogdetails})

@login_required(login_url='/webapp/login/')
def myBlog(request):
    user= get_object_or_404(User,username=request.user)
    blogdetails = blog.objects.filter(Author=user)
    return render(request,'my_blog.html',{'blog':blogdetails})

@login_required(login_url='/webapp/login/')
def updateBlog(request,blog_id):
    c={}
    c['blog_id']=blog_id

    if request.method == "POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        blog.objects.filter(pk=blog_id).update(Title=title, Description=description)
        return redirect('webapp:my_blog')
    
    blog_details=blog.objects.filter(pk=blog_id)
    blog_details=blog_details.values()
    c['Title']=blog_details[0].get('Title')
    c['Description']=blog_details[0].get('Description')
    return render(request,'update_blog.html',c)

@login_required(login_url='/webapp/login/')
def deleteBlog(request,blog_id):
    blog.objects.filter(pk=blog_id).delete()
    return redirect('webapp:my_blog')

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
            return render(request,'login.html')
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
            if 'next' in request.POST:
                next=request.POST.get('next')
                return redirect(next)
            return redirect('webapp:index')
        else:
            c={'error':'Invalid Email or Password. Please try again.', 'email':email, 'password':password}
    return render(request,'login.html',c)

@login_required(login_url='/webapp/login/')
def logout(request):
    auth_logout(request)
    return index(request)

@login_required(login_url='/webapp/login/')
def addBlog(request):
    c={}
    if request.method == "POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        pub_date=datetime.today().strftime("%Y-%m-%d")
        author=get_object_or_404(User,username=request.user)
        new_blog=blog(Title=title,Description=description,Pub_date=pub_date,Author=author)
        new_blog.save()
        return redirect('webapp:my_blog')
    return render(request,'add_blog.html',c)
