from django.shortcuts import render
from django.http import HttpResponse
from .models import dataSolar
from django.core import serializers
from django.http import JsonResponse
import datetime



def index(request):
	#dataSolars = dataSolar.objects.get(id=2)
	obj = dataSolar.objects.all()
	context= {
		"data":obj
	}	
	return render(request, 'index.html', context)


def voltageChart(request):
	today1 = datetime.date.today()
	labels = []
	data = []
	obj = dataSolar.objects.all().filter(days=today1)
	for entry in obj:
		labels.append(entry.hourly)
		data.append(entry.voltage)
	
	return render(request, 'voltageChart.html', {
        'labels': labels,
        'data': data,
        })


def currentChart(request):
	today1 = datetime.date.today()
	obj = dataSolar.objects.all().filter(days=today1)
	context= {
		"data":obj
	}	
	return render(request, 'currentChart.html', context)


def faultChart(request):
	obj = dataSolar.objects.all()
	context= {
		"data":obj
	}	
	return render(request, 'faultChart.html', context)


def powerChart(request):
	obj = dataSolar.objects.all()
	context= {
		"data":obj
	}	
	return render(request, 'powerChart.html', context)


def powerChartt(request):
	today1 = datetime.date.today()
	labels = []
	data = []
	obj = dataSolar.objects.all().values('power','hourly').filter(days=today1)
	for entry in obj:
		labels.append(entry['hourly'])
		data.append(entry['power'])
	return JsonResponse(data={
		'labels': labels,
		'data' : data,
	})	

def currentChartt(request):
	today1 = datetime.date.today()
	labels = []
	data = []
	obj = dataSolar.objects.all().values('currents','hourly').filter(days=today1)
	for entry in obj:
		labels.append(entry['hourly'])
		data.append(entry['currents'])
	return JsonResponse(data={
		'labels': labels,
		'data' : data,
	})	



'''

def voltageChartt(request):
	obj = dataSolar.objects.all()
	data = serializers.serialize('json', obj)
	return HttpResponse(data)
'''