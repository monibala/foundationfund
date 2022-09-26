
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.couses , name="couses"),
    path('category/<slug:cat>', views.couses , name="catcouses"),
    path('couse/<slug:slug>/', views.couses , name="singlecouse"),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
    path('donate/hendlerequest/', views.hendlerequest , name="handle"),
    path('rozor/hendlerequest/', views.rozorpayHandler , name="rozorpayindex"),
    path('rozor/handler/', views.rozorhandler , name="rozorpayhanle"),
    path('donate/<slug:slug>/', views.paymenthandler , name="donate"),
    # path('donate/<slug:slug>/', views.paypalHandler , name="donate"),
]
