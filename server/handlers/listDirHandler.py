# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, request, current_app


def listDirHandler():
    dir_key = current_app.config['dbkeys']['dir']
    dir_capnp_schema = current_app.config['capnp']['dir']
    redis = current_app.config['redis']

    response = list()
    for dir_blob in redis.hvals(dir_key):
        dir_capnp = dir_capnp_schema.from_bytes_packed(dir_blob)
        response.append(dir_capnp.to_dict())

    return jsonify(response), 200, {"Content-type": 'application/json'}
