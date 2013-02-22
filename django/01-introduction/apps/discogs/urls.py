from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from discogs.views import *

urlpatterns = patterns('',
    url(r'^search/$', discogs_search, name='discogs-search'),
)