from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('datalogs', views.DatalogView)
router.register('plants', views.PlantView)
urlpatterns = [
    path('api/', include(router.urls))
]
