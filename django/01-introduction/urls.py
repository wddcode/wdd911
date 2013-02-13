from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       
    url(r'^$', direct_to_template, {'template': 'test.html'}, name='home'),
    # project urls
    url(r'^twitter/', include('twitter.urls')),
    
    # admin urls
    url(r'^admin/', include(admin.site.urls)),
)




if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
)
    
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)