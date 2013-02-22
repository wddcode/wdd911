from django.http import HttpResponse
from django.template.response import TemplateResponse

from lib.api import Twitter

"""
def twitter_search(request):
    print request    
    html = '<h1>Hallo</h1>'
    return HttpResponse(html)
"""

def twitter_search(request):
    
    query = request.GET.get('query', None)
    
    print 'Query: %s' % query
    
    tweets = None
    
    if query:
        t = Twitter()
        result = t.search(query)
        tweets = result['results']
    
    data = {
            'title': 'My Title',
            'query': query,
            'tweets': tweets
            }
    
    return TemplateResponse(request, 'twitter/search.html', data)
