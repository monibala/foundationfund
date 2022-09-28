from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from superuser.forms import GenForm
from .models import VolunteerRegister,joblist
# Create your views here.
def about(request):
    res = {}
    res['volunteer'] = VolunteerRegister.objects.all()
    return render(request,'about/about.html',res)
@csrf_exempt
def volunteer(request):
    res = {}
    res['volunteer'] = VolunteerRegister.objects.all()
    if request.method == "POST":
        resjson = {}
        form = GenForm(VolunteerRegister)
        updated_request = request.POST.copy()
        updated_request.update({'status': 'Applied'})
        form = form(updated_request,request.FILES,)
        if form.is_valid():
            # form.save()
            resjson['status'] = True
            resjson["message"] = "Thanks For Registration We Will Get Back To You Soon :)"
            print("success")
            return JsonResponse(resjson)
        else:
            resjson['status'] = False
            print(form.errors.as_data())
            mes = ""
            for data in form.errors:
                mes+= str(form.errors[data]).replace('This',data)
            resjson['message'] = mes
            return JsonResponse(resjson)
        pass
    return render(request,'about/volunteer.html',res)

def job(request):
    res={}
    res['joblist'] = joblist.objects.all()
    return render(request,'about/job-list.html',res)
