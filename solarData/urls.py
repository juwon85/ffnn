#from django.contrib import admin
from django.urls import path
#from django.conf.urls import url
from .views import index, voltageChart, currentChart, faultChart, powerChart, powerChartt,currentChartt

urlpatterns = [
    path('', index, name='index'),
    path('voltageChart/', voltageChart, name='voltageChart'),
    path('currentChart', currentChart, name='currentChart'),
    path('faultChart', faultChart, name='faultChart'),
    path('powerChart', powerChart, name='powerChart'),
    path('powerChartt', powerChartt, name='powerChartt'),
    path('currentChartt', currentChartt, name='currentChartt'),
]
