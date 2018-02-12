# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, current_app

CLASS='user'

def listUserHandler():
    redis = current_app.config['redis']
    key = current_app.config['dbkeys'][CLASS]
    capnp_schema = current_app.config['capnp'][CLASS]

    response = list()
    for blob in redis.hvals(key):
        capnp_data = capnp_schema.from_bytes_packed(blob)
        response.append(capnp_data.to_dict())

    return jsonify(response), 200, {"Content-type": 'application/json'}
