from django.conf.urls import patterns, include, url
from article.views import HelloTemplate

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #FIRST just demonstrating basic url to view mapping
    #don't have a special urls.py file in our article project folder
    url(r'^hello/$', 'article.views.hello'),
    url(r'^hello_template/$','article.views.hello_template_simple'),
    url(r'^hello_template_simple/$', 'article.views.hello_template_simple'),
    url(r'^hello_class_view/$', HelloTemplate.as_view()),
    
    # url(r'^yt_tut/', include('yt_tut.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
