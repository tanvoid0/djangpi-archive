from django.contrib import admin
# from django.contrib.auth.models import Group
from .models import *

# Register your models here.
admin.site.site_header = "Eco Friend Admin Panel"

class DatalogAdmin(admin.ModelAdmin):
    exclude = ('title')

admin.site.register(Sensor)
admin.site.register(Device)
admin.site.register(Datalog)
admin.site.register(Plant)
