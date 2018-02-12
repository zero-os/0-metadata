# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, current_app

CLASS='bdomain'

def deleteBdomainHandler(id):
    redis = current_app.config['redis']
    key = current_app.config['dbkeys'][CLASS]

    if redis.hdel(key, id) == 1:
        return "", 204, {"Content-type": "application/json"}

    return "", 404, {"Content-type": "application/json"}
