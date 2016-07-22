# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Region, Flowstand, Manufactor, Customer

from django.core.urlresolvers import reverse

class FlowAdmin(admin.ModelAdmin):
	list_display = ['name', 'customer','serial_number', 'flow_range', 'manufactor']
	ordering = ['region']
	list_filter = ['region', 'customer', 'manufactor']
	list_per_page = 15
	search_fields = ['name', 'customer']
	
class CustomerAdmin(admin.ModelAdmin):
	list_display = ['name', 'agent','address', 'contacts']
	ordering = ['region']
	list_filter = ['region']
	list_per_page = 15
	search_fields = ['name', 'agent', 'address']
	
admin.site.register(Region)
admin.site.register(Flowstand, FlowAdmin)
admin.site.register(Manufactor)
admin.site.register(Customer, CustomerAdmin)