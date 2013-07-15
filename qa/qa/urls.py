from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from views import InterviewQuestions

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'views.home'),
    url(r'^login/$', 'views.login'),
    url(r'^userinfo/$', 'views.getuserinfo'),
    url(r'^interview/$', InterviewQuestions.as_view()),
    url(r'^summary/$', 'views.summary'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)   
