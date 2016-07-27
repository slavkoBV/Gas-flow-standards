"""flowstanddb URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
   
   url(r'^$', 'flowstands.views.flowstands_list', name='home'),
	
   url(r'^customers/$', 'flowstands.views.customers_list', name='customers'),
   
   url(r'^manufactors/$', 'flowstands.views.manufactors_list', name='manufactors'),
   
   url(r'^admin/', include(admin.site.urls)),			

]


