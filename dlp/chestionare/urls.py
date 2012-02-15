from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('dlp.chestionare.views',
    url(r'^$', 'index'),
    url(r'^(?P<quest_id>\d+)/$', 'quest'),
    url(r'^(?P<quest_id>\d+)/page/(?P<page_id>\d+)/$', 'page'),
    url(r'^(?P<quest_id>\d+)/page/(?P<page_id>\d+)/answer/$', 'answer'),
    url(r'^(?P<quest_id>\d+)/results/$', 'results')
)
