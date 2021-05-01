from django.contrib import admin
from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path(r'',views.index,name='index'),
    path(r'update',views.update,name='update'),
]