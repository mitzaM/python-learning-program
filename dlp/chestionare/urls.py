from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('dlp.chestionare.views',
    url(r'^$', 'index'),
    url(r'^(?P<test_id>\d+)/$', 'test'),
    url(r'^(?P<test_id>\d+)/page/(?P<page_id>\d+)/$', 'page'),
    url(r'^(?P<test_id>\d+)/results/$', 'results')
)
