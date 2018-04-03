#!/usr/bin/env python3

import time

from flask import jsonify
from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import generate_password_hash, check_password_hash

from hash_api.base import app
from hash_api.models.users import User


@app.route('/api/v<version>/users/create', methods=["POST"])
def register_user(version):
    app.logger.debug(
        f'[!] Received registration request to: \
         {request.path} from: {request.remote_addr}'
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
    new_user = User(
        username=request_json['username'],
        password=generate_password_hash(request_json['password'])
    )
    new_user.save()

    return jsonify({'result': 'success', 'action': 'create'}), 200


@app.route('/api/v<version>/user/auth', methods=["POST"])
def auth_user(version):
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

    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400

    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = User.objects.get(username=username)
    if user and check_password_hash(user.password, password):
        return jsonify(
            {
                'access_token': create_access_token(identity=username),
                'refresh_token': create_refresh_token(identity=username),
                'creation_date': '{}'.format(time.strftime('%m/%d/%YT%H:%M:%SZ'))
            }
        ), 200

    else:
        return jsonify({'msg': 'Invalid Credentials.'}), 401
