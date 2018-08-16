# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Region, Flowstand, Manufactor, Customer, NationalStandard, Documents
from django.contrib.admin import AdminSite


class ByCityFilter(admin.SimpleListFilter):
    title = u'Місто'
    parameter_name = 'city'

    def lookups(self, request, model_admin):
        city_list = set()
        flowstands = Flowstand.objects.all()
        region = request.GET.get('region__id__exact')
        if region:
            flowstands = flowstands.filter(region__id=region)
        for stand in flowstands:
            city = stand.placeholder[stand.placeholder.find('.')+1: stand.placeholder.find(',')]
            city_list.add((city.strip(), city.strip()))
        city_list = sorted(city_list)
        return list(city_list)

    def queryset(self, request, queryset):
        if self.value():
            queryset = queryset.filter(placeholder__contains=self.value())
            for stand in queryset:
                if stand.placeholder[stand.placeholder.find('.')+1: stand.placeholder.find(',')].strip() != self.value():
                    queryset = queryset.exclude(id=stand.id)
        return queryset


class FlowAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'serial_number', 'flow_range', 'region', 'customer', 'manufactor', 'placeholder']}),
        (u'Калібрування', {'fields': ['date_calibr', 'certificate', 'traceability']})
    ]

    list_display = ['name', 'serial_number', 'customer', 'placeholder', 'flow_range', 'date_calibr', 'certificate']
    ordering = ['region']
    list_filter = ['region', 'customer', 'manufactor', ByCityFilter]
    list_per_page = 20
    search_fields = ['name', 'customer__name']
    date_hierarchy = 'date_calibr'


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'agent', 'address', 'contacts']
    ordering = ['region']
    list_filter = ['region']
    list_per_page = 20
    search_fields = ['name', 'agent', 'address']


class NationalStandardAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'name', 'keeper']
    search_fields = ['short_name', 'keeper']


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ['title', 'edition']
    search_fields = ['title']


AdminSite.site_header = u'База еталонів витрати газу'
AdminSite.site_title = u'Адміністрування'

admin.site.register(Region)
admin.site.register(Flowstand, FlowAdmin)
admin.site.register(Manufactor)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(NationalStandard, NationalStandardAdmin)
admin.site.register(Documents, DocumentsAdmin)
