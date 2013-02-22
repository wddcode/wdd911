from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       
    url(r'^$', direct_to_template, {'template': 'home.html'}, name='home'),
    
    url(r'^contact/$', direct_to_template, {'template': 'contact.html'}, name='contact'),
    
    # project urls
    url(r'^twitter/', include('twitter.urls')),
    url(r'^discogs/', include('discogs.urls')),
    url(r'^portfolio/', include('portfolio.urls')),
    
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