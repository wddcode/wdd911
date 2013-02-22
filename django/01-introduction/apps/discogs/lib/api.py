#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os

class Discogs(object):
    
    def __init__(self):
        
        self.api_url = 'http://api.discogs.com/releases/'
        
    def search(self, query):
        
        print 'search for: %s' % query
        query_url = '%s%s' % (self.api_url, query)
        
        print 'url: %s' % query_url
        
        r = requests.get(query_url)
                
        return r.json()
