from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'My_Page.views.home', name='home'),
    # url(r'^My_Page/', include('My_Page.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(/)?$', RedirectView.as_view(url='/landing/')),
    url(r'^chats/', include('Chat.urls')),
    url(r'^landing/', include('Landing.urls')),
    url(r'^servlet/', include('Servlet.urls')),
)
