from django.contrib.auth import authenticate, login
from django.db import models
from django.shortcuts import redirect, render

from about.models import VolunteerRegister
from .models import HomeSlider
from django.http import JsonResponse
from couses.models import Couses
from events.models import Events
from blogs.models import Blog
from about.models import VolunteerRegister
# Create your views here.
def index(request):
    res = {}
    res['sliders'] = HomeSlider.objects.all()
    res['couseslist'] = Couses.objects.all().order_by('-time')
    res['eventlist'] = Events.objects.all().order_by('-eventTime')
    res['volunteerlist'] = VolunteerRegister.objects.all()
    res['bloglist'] = Blog.objects.filter(type="Blog").order_by('-time')
    res['newslist'] = Blog.objects.filter(type="News").order_by('-time')
    
    return render(request,'index.html',res)
def logindashboard(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('dashboardindex')
    if request.method=="POST":
        print(request.POST,"this is working")
        username = request.POST.get('username')
        password = request.POST.get('password')
        USER = authenticate(request,username=username, password=password)
        if USER is not None:
            login(request, USER)
            if request.user.is_superuser:
                return JsonResponse({'status':'ok','msg':'Login Success','next':request.GET.get('next'),'type':'success'})
            return JsonResponse({"status":'invaliduser','msg':'invalid user','type':'danger'})
    return render(request,'logindashboard.html')