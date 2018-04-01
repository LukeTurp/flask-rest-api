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
        app.logger.error(
            f'[-] Received invalid api version: {version}'
        )
        return jsonify(
            {
                "result": "Error",
                "message": "Invalid API version provided.",
                "supported_versions": ['1']
            }
        ), 400

    request_json = request.get_json()
    event = HashEvent(
        abspath=request_json['abspath'],
        filename=request_json['filename'],
        hashvalue=request_json['hashvalue']
    )
    event.save()
    app.logger.info(
        f'[+] Saved event to DB: {event.id}.'
    )
    return jsonify(
        {
            'result': 'success',
            'action': 'create',
            'object': str(event.id),
            'version': version
        }
    ), 200
