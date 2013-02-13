from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from twitter.views import *

urlpatterns = patterns('',
    url(r'^search/$', direct_to_template, {'template': 'twitter/search.html'}, name='twitter-search'),
)