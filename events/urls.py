
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.events , name="events"),
    path('<slug:slug>/', views.events , name="singleevent"),
]
