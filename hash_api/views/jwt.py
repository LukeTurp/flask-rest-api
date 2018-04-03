#!/usr/bin/env python3

import time
from flask import jsonify
from flask import request
from flask_jwt_extended import (
    jwt_required, get_jwt_identity,
    create_access_token, create_refresh_token,
    jwt_refresh_token_required, get_raw_jwt
)

from hash_api.base import jwt, app

blacklist = set()

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


@app.route('/api/v<version>/token/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh(version):
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

    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user),
        'refresh_token': create_refresh_token(identity=current_user),
        'creation_date': '{}'.format(time.strftime('%m/%d/%YT%H:%M:%SZ'))
    }
    return jsonify(ret), 200


@app.route('/api/v<version>/user/logout', methods=['DELETE'])
@jwt_required
def logout(version):
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

    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify({"msg": "Successfully logged out"}), 200
