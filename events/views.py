from django.shortcuts import render
from .models import Events
from django.core.paginator import Paginator
# Create your views here.
def events(request,slug=None):
    res = {}
    if slug is not None:
        #for single event
        res['event'] = Events.objects.get(slug=slug)
        return render(request,'events/single-event.html',res)
    # for event list
    res['events'] = Events.objects.all()
    paginator = Paginator(res['events'], 15) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    res['page_obj'] = paginator.get_page(page_number)
    return render(request,'events/events.html',res)