"""flowstanddb URL Configuration"""

from .settings import MEDIA_ROOT, DEBUG, MEDIA_URL
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [

    url(r'^$', 'flowstands.views.flowstands_list', name='home'),

    url(r'^flowstand/(?P<pk>\d+)/$', 'flowstands.views.flowstand_view', name='flowstand_view'),

    url(r'^customers/$', 'flowstands.views.customers_list', name='customers'),

    url(r'^manufactors/$', 'flowstands.views.manufactors_list', name='manufactors'),

    url(r'^national_standards/$', 'flowstands.views.national_standards', name='national_standards'),

    url(r'^national_standards/(?P<pk>\d+)/$', 'flowstands.views.national_standard', name='national_standard'),

    url(r'^contact/$', 'flowstands.views.contact_admin', name='contact'),

    url(r'^admin/', include(admin.site.urls)),

]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
