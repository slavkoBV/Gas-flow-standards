# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Region, Flowstand, Manufactor, Customer
from django.contrib.admin import AdminSite

from django.core.urlresolvers import reverse

class FlowAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['name','serial_number','flow_range','region','customer', 'manufactor', 'placeholder']}),
		(u'Калібрування', {'fields':['date_calibr', 'certificate', 'traceability']})
		]
	
	list_display = ['name', 'serial_number', 'customer', 'placeholder','flow_range', 'date_calibr', 'certificate']
	ordering = ['region']
	list_filter = ['region', 'customer', 'manufactor','date_calibr']
	list_per_page = 20
	search_fields = ['name', 'customer__name']
	
class CustomerAdmin(admin.ModelAdmin):
	list_display = ['name', 'agent','address', 'contacts']
	ordering = ['region']
	list_filter = ['region']
	list_per_page = 20
	search_fields = ['name', 'agent', 'address']

AdminSite.site_header = u'База еталонів витрати газу'
AdminSite.site_title =u'Адміністрування'
	
admin.site.register(Region)
admin.site.register(Flowstand, FlowAdmin)
admin.site.register(Manufactor)
admin.site.register(Customer, CustomerAdmin)

