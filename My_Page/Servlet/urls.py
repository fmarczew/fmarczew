from django.conf.urls import patterns, url

from Servlet import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
)