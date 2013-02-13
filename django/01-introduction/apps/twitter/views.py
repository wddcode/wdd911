from django.http import HttpResponse
from django.template.response import TemplateResponse

from lib.api import Twitter

def twitter_search(request):
    return HttpResponse('')


"""
def twitter_search(request):
    return TemplateResponse(request, 'twitter/search.html', data)
"""