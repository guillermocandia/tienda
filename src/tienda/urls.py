from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'', include('app.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^payments/', include('solie.payments.urls')),
    url(r'^util/', include('solie.util.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
)
