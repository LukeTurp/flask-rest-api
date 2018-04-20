#!/usr/bin/env python3

from flask import jsonify, request

from hash_api.base import app


@app.route('/', methods=['GET'])
def index():
    app.logger.debug(
        f'[!] Received request to: {request.path} from: {request.remote_addr}'
    )
    return jsonify({'result': 'success'})
