#!/usr/bin/env python3

class HashEvent(object):
    def __init__(self, abspath=None, filename=None, hashvalue=None, rundate=None):
        self.abspath = abspath
        self.filename = filename
        self.hashvalue = hashvalue
        self.rundate = rundate
    
