#!/usr/bin/env python3

from flask import Flask
from flask import jsonify
from hash_api.config.settings import Config

app = Flask(__name__)
config = Config()

import hash_api.views.base
