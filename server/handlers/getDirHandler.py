# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, request, current_app


def getDirHandler(id):
    redis = current_app.config['redis']
    dir_key = current_app.config['dbkeys']['dir']
    dir_schema = current_app.config['capnp']['dir']

    dir_blob = redis.hget(dir_key, id)
    if dir_blob is None:
        return "", 404, {"Content-type": "application/json"}

    dir_capnp = dir_schema.from_bytes_packed(dir_blob)
    return jsonify(dir_capnp.to_dict()), 200, {"Content-type": "application/json"}
