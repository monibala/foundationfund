from django.core.paginator import Paginator
from django.shortcuts import render

from couses.models import Category
from .models import Blog, tags
# Create your views here.
def blogs(request,slug=None,cat=None):

    res= {}
    res['title'] = "Blogs"
    type = 'Blog'
    res['type'] = type.lower()
    res['singleurl'] = "single"+res['type']
    if slug is not None:
        #for single event
        res['blogob'] = Blog.objects.get(slug=slug)
        res['categories'] = Category.objects.filter(Blog__type="Blog").order_by('name')
        return render(request,'blogs/blog-single.html',res)
    res['bloglist'] = Blog.objects.filter(type=type).order_by('-time')
    # for event list
    if cat is not None:
        res['bloglist']= Blog.objects.filter(type=type,category__slug=cat).order_by('-time')
        res['title'] = Category.objects.get(slug=cat).name
    paginator = Paginator(res['bloglist'], 5) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    res['tags'] = tags.objects.all()
    res['page_obj'] = paginator.get_page(page_number)
    return render(request,'blogs/blogs.html',res)
def news(request,slug = None,cat=None,tag=None):
    res= {}
    res['title'] = "News"
    type = 'News'
    res['type'] = type.lower()
    res['singleurl'] = "single"+res['type']
    if slug is not None:
        #for single event
        res['blogob'] = Blog.objects.get(slug=slug)
        res['title'] = res['blogob'].title
        res['categories'] = Category.objects.filter(Blog__type="News").order_by('name')
        return render(request,'blogs/blog-single.html',res)
    # for event list
    res['bloglist'] = Blog.objects.filter(type=type).order_by('-time')
    if cat is not None:
        res['bloglist']= Blog.objects.filter(type=type,category__slug=cat).order_by('-time')
        res['title'] = Category.objects.get(slug=cat).name
    if tag is not None:
        res['bloglist']= Blog.objects.filter(type=type,tags__tags=tag).order_by('-time')
        res['title'] = tag
    paginator = Paginator(res['bloglist'], 5) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    res['page_obj'] = paginator.get_page(page_number)
    res['tags'] = tags.objects.all()
    return render(request,'blogs/blogs.html',res)