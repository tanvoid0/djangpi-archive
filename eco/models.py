from django.db import models

# Create your models here.
from django.template.defaulttags import now

class Sensor(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True, null=True)
    brand = models.CharField(max_length=200, default=None, blank=True, null=True)
    model = models.CharField(max_length=200, default=None, blank=True, null=True)
    description =  models.TextField(default=None, blank=True, null=True)

class Device(models.Model):
    model =  models.CharField(max_length=200, default=None, blank=True, null=True)
    image =  models.CharField(max_length=200, default=None, blank=True, null=True)
    type = models.CharField(max_length=200, default=None, blank=True, null=True)
    sensors = models.CharField(max_length=200, default=None, blank=True, null=True)
    remarks =  models.TextField(default=None, blank=True, null=True)


class Plant(models.Model):
    name = models.CharField(max_length=200, default=None, blank=True, null=True)

    family = models.CharField(max_length=200, default=None, blank=True, null=True)
    genus = models.CharField(max_length=200, default=None, blank=True, null=True)
    species = models.CharField(max_length=200, default=None, blank=True, null=True)
    variety = models.CharField(max_length=200, default=None, blank=True, null=True)
    cultivar = models.CharField(max_length=200, default=None, blank=True, null=True)
    superior_selection = models.CharField(max_length=200, default=None, blank=True, null=True)

    type = models.CharField(max_length=200, default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class Datalog(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, default=1, blank=True, null=True)
    light = models.FloatField(default=None, blank=True, null=True)
    temperature = models.FloatField(default=None, blank=True, null=True)
    humidity = models.FloatField(default=None, blank=True, null=True)
    soil = models.CharField(max_length=200, default=None, blank=True, null=True)
    moisture = models.FloatField(default=None, blank=True, null=True)
    remarks = models.TextField(default=None, blank=True, null=True)
    alive = models.BooleanField(default=True, blank=True, null=True)

    environment = models.BooleanField(default=None, blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, editable=False)

    def __str__(self):
        return self.plant.name

