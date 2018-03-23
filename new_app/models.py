from django.core.validators import RegexValidator
from django.db import models
from django.db.models.aggregates import Sum


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

    def current_weight(self):
        transport = self.transport_set.first()
        if transport:
            weight = transport.elements.aggregate(Sum('weight'))
            if weight.get('weight__sum', 0) is None:
                return 0
            else:
                return weight.get('weight__sum')
        else:
            return 0


class Transport(models.Model):
    elements = models.ManyToManyField(Element)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    weight_left = models.FloatField(null=True)

    def __str__(self):
        return "Plan na zaladunek {}".format(self.vehicle.name)
