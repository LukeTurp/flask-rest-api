#!/usr/bin/env python3
import os

class BaseConfig(object):
    def __init__(self):
        self.debug = True if os.environ['HASH_API_DEBUG'].lower() == 'true' else False
        self.host = os.environ['HASH_API_HOST']
        self.port = int(os.environ['HASH_API_PORT'])
        self.application_secret = os.environ['HASH_APP_SECRET']

class Config(BaseConfig):
    def __init__(self):
        super().__init__()
        self.log_file_abs_path = os.environ['HASH_API_LOG']
        self.mongo_host = os.environ['HASH_MONGO_HOST']
        self.mongo_port = int(os.environ['HASH_MONGO_PORT'])
        self.mongo_user = os.environ['HASH_MONGO_USER']
        self.mongo_pass = os.environ['HASH_MONGO_PASS']
        self.mongo_db_name = os.environ['HASH_MONGO_DB']
        self.jwt_secret = os.environ['HASH_JWT_SECRET']
