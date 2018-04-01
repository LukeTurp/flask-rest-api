#!/usr/bin/env python3

import logging

from flask import Flask
from flask import jsonify
from flask_mongoengine import MongoEngine

from hash_api.config.settings import Config

config = Config()

formatter = logging.Formatter(
    "[%(asctime)s] {line: %(lineno)d} %(levelname)s - %(message)s"
)
handler = logging.FileHandler(config.log_file_abs_path)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

app = Flask(__name__)
app.config['MONGODB_DB'] = config.mongo_db_name
app.config['MONGODB_HOST'] = config.mongo_host
app.config['MONGODB_PORT'] = config.mongo_port
app.config['MONGODB_USERNAME'] = config.mongo_user
app.config['MONGODB_PASSWORD'] = config.mongo_pass

app.logger.addHandler(handler)

db = MongoEngine(app)

@app.after_request
def after_request(response):
    response.headers.add('X-XSS-Protection', '1; mode=block')
    response.headers.add('X-Frame-Options', 'SAMEORIGIN')
    response.headers.add('X-Content-Type-Options', 'nosniff')
    return response

import hash_api.views.base
import hash_api.views.hash_events
