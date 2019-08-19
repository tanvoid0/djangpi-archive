from django.contrib import admin
from .models import Datalog, Plant, Sensor, Device

# Register your models here.
admin.site.register(Sensor)
admin.site.register(Device)
admin.site.register(Datalog)
admin.site.register(Plant)
