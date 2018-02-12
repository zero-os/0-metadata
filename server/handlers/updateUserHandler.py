# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

import json as JSON
import os

import jsonschema
from jsonschema import Draft4Validator

from flask import current_app, jsonify, request

CLASS='user'

<<<<<<< HEAD
dir_path = os.path.dirname(os.path.realpath(__file__))
json_schema = JSON.load(open(dir_path + '/schema/' + CLASS + '_schema.json'))
schema_resolver = jsonschema.RefResolver('file://' + dir_path + '/schema/', json_schema)
schema_validator = Draft4Validator(json_schema, resolver=schema_resolver)
=======
CLASS='user'
>>>>>>> e07e12d... Some refactoring on User and Dir handlers

dir_path = os.path.dirname(os.path.realpath(__file__))
json_schema = JSON.load(open(dir_path + '/schema/' + CLASS + '_schema.json'))
schema_resolver = jsonschema.RefResolver('file://' + dir_path + '/schema/', json_schema)
schema_validator = Draft4Validator(json_schema, resolver=schema_resolver)

def updateUserHandler(id):
    redis = current_app.config['redis']
    key = current_app.config['dbkeys'][CLASS]
    capnp_schema = current_app.config['capnp'][CLASS]

    inputs = request.get_json()
<<<<<<< HEAD
    key = current_app.config['dbkeys'][CLASS]
    capnp_schema = current_app.config['capnp'][CLASS]
=======
>>>>>>> e07e12d... Some refactoring on User and Dir handlers

    try:
        schema_validator.validate(inputs)
    except jsonschema.ValidationError as e:
        return jsonify(errors="bad request body: %s" % e.message), 400

    # create capnp object
    capnp_data = capnp_schema.new_message(**inputs)

    # save new object into kvs
<<<<<<< HEAD
    redis = current_app.config['redis']
    redis.hset(key, str(capnp_data.uid), capnp_data.to_bytes_packed())

    return jsonify(capnp_data.to_dict()), 200, {"Content-type": 'application/json'}
=======
    redis.hset(key, str(capnp_data.uid), capnp_data.to_bytes_packed())

    return jsonify(capnp_data.to_dict()), 200, {"Content-type": "application/json"}
>>>>>>> e07e12d... Some refactoring on User and Dir handlers
