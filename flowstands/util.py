# -*- coding: utf-8 -*-

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginate (objects, size, request, context, var_name='object_list'):
	
	"""Paginate objects provided by view.
	
	This function takes:
		* list of elements;
		* number of objects per page;
		* request object to get url parameters from;
		* context to set  new variables into;
		* var_name - variable name for list of objects.
		
	It returns updated context object.
	"""
	
	# apply pagination
	paginator = Paginator(objects, size)
	
	# try to get page number from request
	page = request.GET.get('page', '1')
	try:
		object_list = paginator.page(page)
	except PageNotAnInteger:
		# if page is not integer, deliver first page
		object_list = paginator.page(1)
	except EmptyPage:
		# if page is out of range (e.g. 9999),
		# deliver last page of results
		objects_list = paginator.page(paginator.num_pages)
		
	# set variables into context
	context[var_name] = object_list
	context['is_paginated'] = object_list.has_other_pages()
	context['page_obj'] = object_list
	context['paginator'] = paginator
	
	return context

def get_regions(request):
	"""Return list of existing regions"""
	# deferred import of Region model to avoid cycled imports
	from .models import Region
	
	# get currently selected region
	cur_region = get_current_region(request)
	
	regions = []
	for region in Region.objects.all().order_by('name'):
		regions.append({
		'id': region.id,
		'name': region.name,
		'selected': cur_region and cur_region.id == region.id and True or False
		})
	return regions

def get_current_region(request):
	"""Returns currently selected region or None"""
	
	# we remember selected region in a cookie
	pk = request.COOKIES.get('current_region')
	
	if pk:
		from .models import Region
		try:
			region = Region.objects.get(pk=int(pk))
		except Region.DoesNotExist:
			return None
		else:
			return region
	else:
		return None