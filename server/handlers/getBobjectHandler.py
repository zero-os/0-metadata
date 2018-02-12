# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, current_app

CLASS='bobject'

def getBobjectHandler(id):
    redis = current_app.config['redis']
    key = current_app.config['dbkeys'][CLASS]
    capnp_schema = current_app.config['capnp'][CLASS]

    blob = redis.hget(key, id)
    if blob is None:
        return "", 404, {"Content-type": "application/json"}

    data = capnp_schema.from_bytes_packed(blob)
    return jsonify(data.to_dict()), 200, {"Content-type": "application/json"}
