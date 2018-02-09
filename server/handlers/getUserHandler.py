# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, current_app


def getUserHandler(id):

    # get capnp encoded users list
    redis = current_app.config['redis']
    user_key = current_app.config['dbkeys']['user']
    user_schema = current_app.config['capnp']['user']

    user_blob = redis.hget(user_key, id)
    if user_blob is None:
        return "", 404, {"Content-type": "application/json"}

    user = user_schema.from_bytes_packed(user_blob)
    return jsonify(user.to_dict()), 200, {"Content-type": "application/json"}
