#!/usr/bin/env python3

from flask import jsonify
from flask import request
from hash_api.base import app

from hash_api.models.hash_events import HashEvent

@app.route('/api/<version>/events/create', methods=['POST'])
def create_event(version):
    app.logger.debug(
        f'[!] Received request to: {request.path} from: {request.remote_addr}'
    )
    if version is not '1':
        return jsonify(
            {
                "result": "Error",
                "message": "Invalid version provided."
            }
        ), 400

    request_json = request.get_json()
    event = HashEvent(
        abspath=request_json['abspath'],
        filename=request_json['filename'],
        hashvalue=request_json['hashvalue'],
        rundate=request_json['rundate']
    )

    return jsonify(
        {
            'result': 'success',
            'version': version,
            'data': event.__dict__
        }
    ), 200
