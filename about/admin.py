from django.contrib import admin

from about.models import ContactInfo, VolunteerRegister, openingHours, joblist

# Register your models here.
admin.site.register(openingHours)
admin.site.register(ContactInfo)
admin.site.register(VolunteerRegister)
admin.site.register(joblist)