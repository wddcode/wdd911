from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from portfolio.views import *

urlpatterns = patterns('',
    url(r'^$', project_list, name='portfolio-project-list'),
)