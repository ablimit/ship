from django.conf.urls import patterns, include, url
from django.conf.urls.static import static


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'views.home'),	
    url(r'^linkedinprofile/$', 'views.linkedinlogin'),
    url(r'^interview1/$', 'views.start1'),
    url(r'^interview2/$', 'views.start2'),
    url(r'^interview3/$', 'views.start3'),
    url(r'^interview4/$', 'views.start4'),
    url(r'^interview5/$', 'views.start5'),
    url(r'^feedback/$', 'views.feedback'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)   
