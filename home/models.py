from django.db import models

# Create your models here.
class HomeSlider(models.Model):
    img = models.ImageField(upload_to= "homeslider")
    title = models.CharField(max_length=40)
    subtitle = models.CharField(max_length=50)
    shortDiscription = models.TextField(max_length=120)