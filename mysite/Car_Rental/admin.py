from django.contrib import admin

# Register your models here.

from .models import Car, Details, User_profile, Car_availability

admin.site.register(User_profile)
admin.site.register( Car)
admin.site.register( Details)
admin.site.register( Car_availability)

