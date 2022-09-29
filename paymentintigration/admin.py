from django.contrib import admin

from paymentintigration.models import PaytmConfig, paypalConfig

# Register your models here.
admin.site.register(PaytmConfig)
admin.site.register(paypalConfig)
