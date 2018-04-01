#!/usr/bin/env python3

import logging

from flask import Flask
from flask import jsonify

from hash_api.config.settings import Config

config = Config()

formatter = logging.Formatter(
    "[%(asctime)s] {line: %(lineno)d} %(levelname)s - %(message)s"
)
handler = logging.FileHandler(config.log_file_abs_path)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

app = Flask(__name__)
app.logger.addHandler(handler)

@app.after_request
def after_request(response):
    response.headers.add('X-XSS-Protection', '1; mode=block')
    response.headers.add('X-Frame-Options', 'SAMEORIGIN')
    response.headers.add('X-Content-Type-Options', 'nosniff')
    return response

import hash_api.views.base
import hash_api.views.hash_events
