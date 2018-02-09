# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, current_app


def deleteDirHandler(id):
    redis = current_app.config['redis']
    dir_key = current_app.config['dbkeys']['dir']

    redis.hdel(dir_key, id)

    return "", 204, {"Content-type": "application/json"}
