
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.about , name='about' ),
    path('become-volunteer/', views.volunteer , name='volunteer' ),
    path('job/', views.job , name='job' ),
]
