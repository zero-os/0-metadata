# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, current_app


def listUserHandler():
    # get capnp encoded users list
    redis = current_app.config['redis']
    user_key = current_app.config['dbkeys']['user']
    user_schema = current_app.config['capnp']['user']

    users_blob = redis.hgetall(user_key)

    response = list()

    for user_blob in users_blob.values():
        user = user_schema.from_bytes_packed(user_blob)
        response.append(user.to_dict())

    return jsonify(response), 200, {"Content-type": 'application/json'}
