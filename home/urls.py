
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('',views.index,name="home"),
    path('logindashboard', views.logindashboard, name="logindashboard"),
]
