from django.contrib import admin

from about.models import ContactInfo, openingHours

# Register your models here.
admin.site.register(openingHours)
admin.site.register(ContactInfo)