from django.contrib import admin
from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path(r'',views.index,name='index'),
    path(r'user_blog/',views.userBlog,name='user_blog'),
    path(r'register/',views.register,name='register'),
    path(r'update_blog/<int:id>/',views.updateBlog,name='update_blog'),
    path(r'delete_blog/<int:id>/',views.deleteBlog,name='delete_blog'),
]