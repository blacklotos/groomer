from django.conf.urls import patterns, include, url
from django.contrib import admin, admindocs
from django.views.generic import TemplateView
from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(selfself,request, user):
        return '/'

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'groomer.views.home', name='home'),
    # url(r'^groomer/', include('groomer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #URL for home page
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    #URL to register, Login and Loguot
        url(r'^login/','django.contrib.auth.views.login',name='login'),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
    #URL forprofile
    url(r'^accounts/profile/', TemplateView.as_view(template_name='profile.html'),name='profile'),
)



