from django.conf.urls import patterns, include, url
from django.contrib import admin, admindocs

# Uncomment the next two lines to enable the admin:

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'groomer.views.home', name='home'),
    # url(r'^groomer/', include('groomer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^accounts/', include('registration.backends.simple.urls')),
)
