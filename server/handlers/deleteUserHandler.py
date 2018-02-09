# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, current_app


def deleteUserHandler(id):
    redis = current_app.config['redis']
    user_key = current_app.config['dbkeys']['user']

    if redis.hdel(user_key, id) == 1:
        return "", 204, {"Content-type": "application/json"}

    return "", 404, {"Content-type": "application/json"}
