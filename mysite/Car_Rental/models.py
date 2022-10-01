from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    photo = models.ImageField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

class Details(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    availability = models.BooleanField()
    price_day = models.IntegerField(default=100)
    
    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Details'
        verbose_name_plural = 'Details'


class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user) + ' account'

    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'User profile'



# class Car_availability(models.Model):
#      = models.OneToOneField(Details, on_delete=models.CASCADE)
#     money = models.IntegerField(default=0)

#     def __str__(self):
#         return str(self.user) + ' account'

#     class Meta:
#         verbose_name = 'User profile'
#         verbose_name_plural = 'User profile'