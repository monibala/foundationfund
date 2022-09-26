from django.db import models
from django.db.models.enums import Choices
from django.core.exceptions import ValidationError
 # paste in your models.py
def only_int(value):
    excep = ["+","-",","]
    for data in excep: value=value.replace(data,'')
    if value.isdigit()==False:
        raise ValidationError('ID contains characters')
# Create your models here.
class VolunteerRegister(models.Model):
    choices = (
        ( 'Applied','Applied' ),
        ( 'Reviewed','Reviewed' ),
        ( 'Pending','Pending' ),
        ( 'Verified','Verified' ),
    )
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)
    branch = models.CharField(max_length=40)
    message = models.CharField(max_length=40)
    resume = models.FileField(upload_to='resume')
    status = models.CharField(max_length=20,choices=choices,default="Applied")
class ContactInfo(models.Model):
    logo = models.ImageField(upload_to = "logo")
    footerlogo = models.ImageField(upload_to = "logo")
    address = models.TextField()
    phone = models.CharField(max_length=15,validators=[only_int])
    email = models.EmailField(max_length=100)
    website = models.CharField(blank=True,max_length=100)
    otherPhone = models.CharField(max_length=1000,help_text="Separate phone number with (,) Ex: +61 3 1234 5678 , +12 3 1234 5678.......",)
class openingHours(models.Model):
    day = models.CharField(max_length=100, help_text="Eg:Mon - Tues :")
    time = models.CharField(max_length=100, help_text="Eg:6.00 am - 10.00 pm or closed")