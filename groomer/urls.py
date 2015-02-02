from django.conf.urls import patterns, include, url
from django.contrib import admin, admindocs
from django.views.generic import TemplateView

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


    #url(r'^$', TemplateView.as_view(template_name="base.html")),

    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^accounts/',include('registration.backends.simple.urls')),
    url(r'^accounts/profile/', TemplateView.as_view(template_name='profile.html'),    name='profile'),
    url(r'^login/','django.contrib.auth.views.login',name='login')
)



