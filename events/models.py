from django.db import models
from django.db.models.base import Model
from ckeditor_uploader.fields import RichTextUploadingField
from couses.models import unique_slug_generator
# Create your models here.
from couses.models import Category

class Events(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE , related_name="Events")
    img = models.ImageField(upload_to="eventImg")
    title = models.CharField(max_length=100)
    topics = models.CharField(max_length=200)
    shortDes = models.CharField(max_length=70)
    content = RichTextUploadingField()
    host = models.CharField(max_length=50)
    eventTime = models.DateTimeField()
    eventEndTime = models.DateTimeField()
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50 ,)
    zip = models.CharField(max_length=10 ,)
    Address = models.CharField(max_length=500)
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = unique_slug_generator(Events,self.title)
        super(Events, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.title)
class eventImg(models.Model):
    event = models.ForeignKey(Events,on_delete=models.CASCADE,related_name="eventImg")
    img = models.ImageField(upload_to="eventImg")








































