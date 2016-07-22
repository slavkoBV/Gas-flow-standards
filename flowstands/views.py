# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from .models import Region, Flowstand, Manufactor, Customer

from .util import paginate, get_current_region

# Flow standarts Views 

def flowstands_list(request):
	current_region = get_current_region(request)
	if current_region:
		flowstands = Flowstand.objects.filter(region = current_region)
	else:
		flowstands = Flowstand.objects.all()
		
	# apply pagination, 6 students per page
	context = paginate(flowstands, 8, request, {}, var_name='flowstands')
	
	return render(request, 'flowstands/flowstands_list.html', context)

# Customers Views

def customers_list(request):
	current_region = get_current_region(request)
	if current_region:
		customers = Customer.objects.filter(region = current_region)
	else:
		customers = Customer.objects.all()
	
	# apply pagination, 6 students per page
	context = paginate(customers, 8, request, {}, var_name='customers')
	
	return render(request, 'flowstands/customers_list.html', context)

#Manufactors Views

def manufactors_list(request):
	manufactors = Manufactor.objects.all()
	# apply pagination, 6 students per page
	context = paginate(manufactors, 8, request, {}, var_name='manufactors')
	return render(request, 'flowstands/manufactors_list.html', context)