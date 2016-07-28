from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Car(models.Model):
    owner = models.ManyToManyField(Owner)  # for exp: family car
    engine = models.ForeignKey(Engine)
    manufacturer = models.ForeignKey(Manufacturer)
    model = models.CharField(max_length=20)
    body_type = models.CharField(max_length=10)
    year_of_issue = models.IntegerField()
    serial_number = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return '{} - {} - {}'.format(self.owner, self.manufacturer, self.model)


class Owner(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=20)
    year_of_birth = models.IntegerField()


class Engine(models.Model):
    capacity = models.FloatField(max_length=5)
    type = models.CharField(max_length=15)
    number_of_cylinders = models.IntegerField()


class Manufacturer(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    founding_date = models.DateField()
