# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, current_app

CLASS='user'

def getUserHandler(id):
    redis = current_app.config['redis']
    key = current_app.config['dbkeys'][CLASS]
    capnp_schema = current_app.config['capnp'][CLASS]

    blob = redis.hget(key, id)
    if blob is None:
        return "", 404, {"Content-type": "application/json"}

    data = capnp_schema.from_bytes_packed(blob)
<<<<<<< HEAD
<<<<<<< HEAD
    return jsonify(data.to_dict()), 200, {"Content-type": "application/json"}
=======
    return jsonify(data.to_dict()), 200, {"Content-type": "application/json"}
>>>>>>> e07e12d... Some refactoring on User and Dir handlers
=======
    return jsonify(data.to_dict()), 200, {"Content-type": "application/json"}
>>>>>>> e07e12d... Some refactoring on User and Dir handlers
