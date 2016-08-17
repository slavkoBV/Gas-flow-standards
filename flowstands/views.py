﻿# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from .models import Region, Flowstand, Manufactor, Customer
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .util import paginate, get_current_region

# Flow standarts Views 

def flowstands_list(request):
	flowstands = Flowstand.objects.all()
	# кількість еталонів у базі
	count = len(flowstands)
	# визначення поточного регіону
	current_region = get_current_region(request)
	if current_region:
		flowstands = Flowstand.objects.filter(region = current_region)
	else:
		flowstands = Flowstand.objects.all()
	# реалізація пошуку
	q = ''
	if request.GET.get('q') <> None:
		q = request.GET['q']
		flowstands = flowstands.filter(Q(customer__name__icontains=q) | Q(name__icontains=q))
		
	# пагінація
	paginator = Paginator(flowstands, 15)
	
	# try to get page number from request
	page = request.GET.get('page')
	try:
		flowstands = paginator.page(page)
	except PageNotAnInteger:
		# if page is not integer, deliver first page
		flowstands = paginator.page(1)
	except EmptyPage:
		# if page is out of range (e.g. 9999),
		# deliver last page of results
		flowstands = paginator.page(paginator.num_pages)		
		
	return render(request, 'flowstands/flowstands_list.html', 
		{'flowstands': flowstands, 'q': q, 'count': count})
########################################################################

# Customers Views

def customers_list(request):
	current_region = get_current_region(request)
	if current_region:
		customers = Customer.objects.filter(region = current_region)
	else:
		customers = Customer.objects.all()
	
	# apply pagination
	paginator = Paginator(customers, 15)
	
	# try to get page number from request
	page = request.GET.get('page')
	try:
		customers = paginator.page(page)
	except PageNotAnInteger:
		# if page is not integer, deliver first page
		customers = paginator.page(1)
	except EmptyPage:
		# if page is out of range (e.g. 9999),
		# deliver last page of results
		customers = paginator.page(paginator.num_pages)	
	
	return render(request, 'flowstands/customers_list.html', 
		{'customers': customers})
#############################################################

#Manufactors Views

def manufactors_list(request):
	manufactors = Manufactor.objects.all()
	context = paginate(manufactors, 15, request, {}, var_name='manufactors')
	return render(request, 'flowstands/manufactors_list.html', context)