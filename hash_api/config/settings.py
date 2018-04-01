#!/usr/bin/env python3

class BaseConfig(object):
    def __init__(self):
        self.debug = True
        self.host = '127.0.0.1'
        self.port = 8000

class Config(BaseConfig):
    def __init__(self):
        super().__init__()
        
