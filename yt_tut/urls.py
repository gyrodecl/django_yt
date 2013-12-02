from django.conf.urls import patterns, include, url
#from article.views import HelloTemplate

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
#autodiscover looks through models in our app
#to see which ones should be shown in the admin interface

#for form-wizard
from yt_tut.forms import ContactForm1, ContactForm2, ContactForm3
from yt_tut.views import ContactWizard

import settings

'''
now with application-specific views
'''

urlpatterns = patterns('',
    url(r'^articles/',include('article.urls')),
    
    # url(r'^yt_tut/', include('yt_tut.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #user auth urls
    url(r'^accounts/login/$',   'yt_tut.views.login'),
    url(r'^accounts/auth/$',    'yt_tut.views.auth_view'),
    url(r'^accounts/logout/$',  'yt_tut.views.logout'),
    url(r'^accounts/loggedin/$','yt_tut.views.loggedin'),
    url(r'^accounts/invalid/$', 'yt_tut.views.invalid_login'),
    url(r'^accounts/register/$','yt_tut.views.register_user'),
    url(r'^accounts/register_success/$', 'yt_tut.views.register_success'),
    url(r'^contact/$', ContactWizard.as_view([ContactForm1,ContactForm2,ContactForm3])),    #list of forms we wantin wizard
)
#if not in DEBUG, then serving online so need to import
#the static urls
if not settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    
    urlpatterns += staticfiles_urlpatterns()