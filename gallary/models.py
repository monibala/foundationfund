from django.db import models

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Image(models.Model):
    gallery = models.ForeignKey(Gallery,on_delete=models.CASCADE,related_name="Image")
    img = models.ImageField(upload_to="GalleryImages")