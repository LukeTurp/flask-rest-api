#!/usr/bin/env python3

from flask import jsonify
from flask import request
from flask_jwt_extended import jwt_required

from hash_api.base import app
from hash_api.models.hash_events import HashEvent

@app.route('/api/v<version>/events/create', methods=['POST'])
@jwt_required
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
    records_to_insert = [
        HashEvent(
            abspath=x['abspath'],
            filename=x['filename'],
            hashvalue=x['hashvalue']
        )
        for x in request_json
    ]
    HashEvent.objects.insert(records_to_insert)

    app.logger.info(
        '[+] Events saved to DB: {0}'.format(len(records_to_insert))
    )
    return jsonify(
        {
            'result': 'success',
            'action': 'create',
            'events_processed': len(records_to_insert),
            'version': version
        }
    ), 200
