from rest_framework import serializers
from .models import Datalog, Plant


class DatalogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Datalog
        fields = ('id', 'url', 'plant', 'light', 'temperature', 'humidity', 'soil', 'moisture', 'remarks', 'alive')

class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant
        fields = ('id', 'url', 'name', 'type', 'description')