"""flowstanddb URL Configuration"""

from .settings import MEDIA_ROOT, DEBUG, MEDIA_URL
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView, TemplateView
from django.contrib.auth.decorators import login_required
from flowstanddb.views import editProfileView, user_list


urlpatterns = [

    url(r'^$', 'flowstands.views.flowstands_list', name='home'),

    url(r'^flowstand/(?P<pk>\d+)/$', 'flowstands.views.flowstand_view', name='flowstand_view'),

    url(r'^customers/$', 'flowstands.views.customers_list', name='customers'),

    url(r'^manufactors/$', 'flowstands.views.manufactors_list', name='manufactors'),

    url(r'^national_standards/$', 'flowstands.views.national_standards', name='national_standards'),

    url(r'^national_standards/(?P<pk>\d+)/$', 'flowstands.views.national_standard', name='national_standard'),

    url(r'^contact/$', 'flowstands.views.contact_admin', name='contact'),

# User Related urs:
    url(r'^user_list/$', user_list, name='user_list'),
    url(r'^users/profile/(?P<pk>\d+)/edit/$', login_required(editProfileView.as_view()), name='profile_edit'),
    url(r'^users/profile/$', login_required(TemplateView.as_view(template_name='registration/profile.html')),
      name='profile'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page':'home'},
          name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'),
          name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls', namespace='users')),

    url(r'^admin/', include(admin.site.urls)),

]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
