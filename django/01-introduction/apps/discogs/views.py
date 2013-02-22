from django.http import HttpResponse
from django.template.response import TemplateResponse

from lib.api import Discogs

"""
def twitter_search(request):
    print request    
    html = '<h1>Hallo</h1>'
    return HttpResponse(html)
"""

def discogs_search(request):
    
    query = request.GET.get('query', None)
    
    print 'Query: %s' % query
    
    release = None
    """"""
    if query:
        d = Discogs()
        result = d.search(query)
        release = result
        
        print release
    
    data = {
            'title': 'My Title Discogs',
            'query': query,
            'release': release
            }
    
    return TemplateResponse(request, 'discogs/search.html', data)
