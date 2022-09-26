from about.models import ContactInfo,openingHours
from blogs.models import Blog
def regfunc(request):
    res = {}
    res['OpeningHour'] = openingHours.objects.all().order_by("id")
    res['latestnews'] = Blog.objects.filter(type='News').order_by('-time')
    try:
       res['info'] = ContactInfo.objects.all()[0]
    except Exception as e:
       res['info'] = []
    return res