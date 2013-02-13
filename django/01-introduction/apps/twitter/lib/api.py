#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os

class Twitter(object):
    
    def __init__(self):
        
        self.api_url = 'http://search.twitter.com/search.json?q='
        
    def search(self, query):
        
        print 'search for: %s' % query
        query_url = '%s%s' % (self.api_url, query)
        
        r = requests.get(query_url)
                
        return r.json()
