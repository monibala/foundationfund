from django.shortcuts import render
from . models import Gallery
# Create your views here.
def gallary(request):
    res = {}
    res['images'] = Gallery.objects.all()
    return render(request,'gallary/gallary1.html',res)
    # return render(request,'gallary/gallary.html')