#!/usr/bin/env python3
from flask import jsonify
from hash_api.base import app

@app.route('/', methods=['GET'])
def index():
    return jsonify({'result': 'success'})
