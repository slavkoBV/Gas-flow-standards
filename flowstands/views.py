# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from .models import Region, Flowstand, Manufactor, Customer
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date, timedelta

from .util import paginate, get_current_region


##########################################################################

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
		flowstands = flowstands.filter(Q(customer__name__icontains=q)
		| Q(name__icontains=q))
	today = date.today()
	
	# пагінація
	paginator = Paginator(flowstands, 15)
	page = request.GET.get('page')
	try:
		flowstands = paginator.page(page)
	except PageNotAnInteger:
		flowstands = paginator.page(1)
	except EmptyPage:
		flowstands = paginator.page(paginator.num_pages)		
	
	# digg-paginator realization
	page_range = []
	ON_EACH_SIDE = 2
	ON_ENDS = 3
	DOT = '...'
	page_num = flowstands.number
	page_range = []
	
	if paginator.num_pages <= 5:
		page_range = range(1, paginator.num_pages + 1)
	else:
		page_range = []
		if page_num > (ON_EACH_SIDE + ON_ENDS):
			page_range.extend(range(1, ON_ENDS))
			page_range.append(DOT)
			page_range.extend(range(page_num - ON_EACH_SIDE, page_num + 1))
		else:
			page_range.extend(range(1, page_num + 1))
		if page_num < (paginator.num_pages - ON_EACH_SIDE - ON_ENDS - 1):
			page_range.extend(range(page_num + 1, page_num + ON_EACH_SIDE + 1))
			page_range.append(DOT)
			page_range.extend(range(paginator.num_pages - ON_ENDS, paginator.num_pages+1))
		else:
			page_range.extend(range(page_num + 1, paginator.num_pages+1))
	
	return render(request, 'flowstands/flowstands_list.html', {
		'flowstands': flowstands,
		'q': q,
		'count': count,
		'today': today,
		'page_range': page_range,
		'DOT': DOT
		}
	)
########################################################################
# Flowstand Detail Views

def flowstand_view(request, pk):
	flowstand = Flowstand.objects.get(id = pk)
	today = date.today()
	# calculation of certificate expiration date
	delta = timedelta(days=365)
	expir_date = flowstand.date_calibr + delta
	diff = (today - flowstand.date_calibr).days
	diff = 365 - int(diff)

	return render(request, 'flowstands/flowstand_view.html', {
		'flowstand':flowstand,
		'today':today,
		'expir_date': expir_date,
		'diff': diff
		}
	)
##########################################################################

# Customers Views

def customers_list(request):
	current_region = get_current_region(request)
	if current_region:
		customers = Customer.objects.filter(region = current_region)
	else:
		customers = Customer.objects.all()
	
	paginator = Paginator(customers, 15)
	page = request.GET.get('page')
	try:
		customers = paginator.page(page)
	except PageNotAnInteger:
		customers = paginator.page(1)
	except EmptyPage:
		customers = paginator.page(paginator.num_pages)	
	
	# digg-paginator realization
	page_range = []
	ON_EACH_SIDE = 2
	ON_ENDS = 3
	DOT = '...'
	page_num = customers.number
	page_range = []
	
	if paginator.num_pages <= 5:
		page_range = range(1, paginator.num_pages + 1)
	else:
   		page_range = []
		if page_num > (ON_EACH_SIDE + ON_ENDS):
			page_range.extend(range(1, ON_ENDS))
			page_range.append(DOT)
			page_range.extend(range(page_num - ON_EACH_SIDE, page_num + 1))
		else:
			page_range.extend(range(1, page_num + 1))
		if page_num < (paginator.num_pages - ON_EACH_SIDE - ON_ENDS - 1):
			page_range.extend(range(page_num + 1, page_num + ON_EACH_SIDE + 1))
			page_range.append(DOT)
			page_range.extend(range(paginator.num_pages - ON_ENDS, paginator.num_pages+1))
		else:
			page_range.extend(range(page_num + 1, paginator.num_pages+1))
	
	return render(request, 'flowstands/customers_list.html', {
		'customers': customers,
		'page_range': page_range,
		'DOT': DOT
		}
	)
#############################################################

#Manufactors Views

def manufactors_list(request):
	manufactors = Manufactor.objects.all()
	context = paginate(manufactors, 15, request, {}, var_name='manufactors')
	return render(request, 'flowstands/manufactors_list.html', context)