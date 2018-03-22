from django.core.validators import RegexValidator
from django.db import models


class Element(models.Model):
    name = models.CharField(max_length=32)
    weight = models.FloatField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Obstacle(models.Model):
    name = models.CharField(max_length=32)
    elements = models.ManyToManyField(Element)
    color = models.CharField(max_length=7,
                             unique=True,
                             validators=[RegexValidator(regex=r'^#(?:[0-9a-fA-F]{3}){1,2}$',
                                                        message='Color must be in HEXADECIMAL symbol')])


class Vehicle(models.Model):
    name = models.CharField(max_length=32)
    capacity = models.FloatField()
    image = models.ImageField(blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.name


#  model pod algorytm
class Transport(models.Model):
    elements = models.ManyToManyField(Element)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return "Plan na zaladunek {}".format(self.vehicle.name)
