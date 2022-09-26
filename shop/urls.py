
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.shops , name="shop"),
    path('<slug:slug>/', views.shops , name="singleshop"),
]
