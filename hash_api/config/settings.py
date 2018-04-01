#!/usr/bin/env python3
import os

class BaseConfig(object):
    def __init__(self):
        self.debug = os.environ['HASH_API_DEBUG']
        self.host = os.environ['HASH_API_HOST']
        self.port = int(os.environ['HASH_API_PORT'])

class Config(BaseConfig):
    def __init__(self):
        super().__init__()
        self.log_file_abs_path = os.environ['HASH_API_LOG']
