from django import template
from blogs.models import Blog
register = template.Library()


@register.filter(name='getlatestnews')
def getlatestnews(value):
    return Blog.objects.filter(type="News").order_by('-time')
@register.filter(name='split')
def split(value,arg):
    return value.split(arg)