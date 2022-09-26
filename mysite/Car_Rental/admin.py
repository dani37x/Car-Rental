from django.contrib import admin

# Register your models here.

from .models import Car, Details

admin.site.register( Car)
admin.site.register( Details)

