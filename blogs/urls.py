
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.blogs , name="blogs"),
    path('news/', views.news , name="news"),
    path('news/<slug:slug>/', views.news , name="singlenews"),
    path('news/<slug:cat>/category/', views.news , name="catnews"),
    path('news/<slug:tag>/tag/', views.news , name="tagnews"),
    path('<slug:slug>/', views.blogs , name="singleblog"),
    path('<slug:cat>/category/', views.blogs , name="catblog"),
    path('<slug:tag>/tag/', views.blogs , name="tagblog"),
]
