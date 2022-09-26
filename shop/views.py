from django.shortcuts import render

# Create your views here.
def shops(request,slug=None):
    if slug is not None:
        #for single shop
        return render(request,'shops/single-shop.html')
    # for shop list
    return render(request,'shops/shops.html')