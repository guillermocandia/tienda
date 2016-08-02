from django.conf.urls import patterns, url

from solie.util import views

urlpatterns = patterns('',
    url(r'^slide/$', views.slide, name='slide'),
)