from django.http import HttpResponse
from django.template.response import TemplateResponse

from lib.api import Twitter

def twitter_search__(request):
    return HttpResponse('')

def twitter_search(request):
    
    query = request.POST.get('query', None)
    
    if query and len(query) < 2:
        query = None
    
    print 'Query: %s' % query
    
    tweets = None
    error = None
    if query:
        t = Twitter()
        try:
            result = t.search(query)
            tweets = result['results']
        except Exception, e:
            error = e
            pass

    
    data = {
            'query': query,
            'tweets': tweets,
            'error': error
            }
    
    return TemplateResponse(request, 'twitter/search.html', data)