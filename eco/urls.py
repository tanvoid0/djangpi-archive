from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('datalogs', views.DatalogView)
router.register('plants', views.PlantView)
urlpatterns = [
    path('', views.HomepageView.as_view(), name='index'),
    path('test/', views.test),
    path('api/', include(router.urls)),
    path('api/range', views.range, name='range')
]
