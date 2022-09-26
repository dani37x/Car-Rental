from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    photo = models.ImageField()

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
    
    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Details'
        verbose_name_plural = 'Details'

