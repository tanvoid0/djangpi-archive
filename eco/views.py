from django.http import HttpResponse, request
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Datalog, Plant
from .serializers import DatalogSerializer, PlantSerializer
import json
from urllib.request import urlopen
import pandas as pd
import requests
import numpy as np

def soilTest(value):
    if value == 0:
        return 'Dry'
    elif value == 1:
        return 'Wet'
    elif value == 2:
        return 'Very Wet'
    else:
        return ''

def test(request):
    return HttpResponse(request)

def range(request):

    # return HttpResponse("Hello")
    # uri = request.get_raw_uri()
    # uri.replace('range')
    # return HttpResponse(uri)
    # url = "http://"+request.get_host()+"/api/datalogs/"
    url = request.GET['url']
    datalogs = requests.get(url=url).json()

    data_frame = pd.DataFrame(datalogs, columns=['id', 'light', 'temperature', 'humidity', 'soil', 'moisture', 'alive'])
    # return render_template("index.html", data=data_frame)
    data_frame_filter = data_frame.query('alive!=0')
    data_frame_filter['soil'] = np.where(data_frame_filter['soil'] == 'Dry', 0, data_frame_filter['soil'])
    data_frame_filter['soil'] = np.where(data_frame_filter['soil'] == 'Wet', 1, data_frame_filter['soil'])
    data_frame_filter['soil'] = np.where(data_frame_filter['soil'] == 'Very Wet', 2, data_frame_filter['soil'])

    # return render_template("index.html", data=data_frame_filter)

    data = {
        'light': [
            data_frame_filter['light'].min(),
            data_frame_filter['light'].max()
        ],
        'temperature': [
            data_frame_filter['temperature'].min(),
            data_frame_filter['temperature'].max()
        ],
        'humidity': [
            data_frame_filter['humidity'].min(),
            data_frame_filter['humidity'].max()
        ],
        'soil': [
            soilTest(data_frame_filter['soil'].min())
            ,
            soilTest(data_frame_filter['soil'].max())
        ],
        'moisture': [
            data_frame_filter['moisture'].min(),
            data_frame_filter['moisture'].max()
        ]
    }
    return HttpResponse(json.dumps(data))
    #
    # print("Light: ", end="")
    # print(data_frame_filter['light'].min(), end=" - ")
    # print(data_frame_filter['light'].max())
    #
    # print("Temperature: ", end="")
    # print(data_frame_filter['temperature'].min(), end=" - ")
    # print(data_frame_filter['temperature'].max())
    #
    # print("humidity: ", end="")
    # print(data_frame_filter['humidity'].min(), end=" - ")
    # print(data_frame_filter['humidity'].max())
    #
    # print("moisture: ", end="")
    # print(data_frame_filter['moisture'].min(), end=" - ")
    # print(data_frame_filter['moisture'].max())

class HomepageView(TemplateView):
    template_name = "index.html"

class DatalogView(viewsets.ModelViewSet):
    queryset = Datalog.objects.all()
    serializer_class = DatalogSerializer

class PlantView(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer