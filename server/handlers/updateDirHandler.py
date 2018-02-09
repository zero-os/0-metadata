# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

import json as JSON
import os

import jsonschema
from jsonschema import Draft4Validator

from flask import current_app, jsonify, request

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_schema = JSON.load(open(dir_path + '/schema/dir_schema.json'))
dir_schema_resolver = jsonschema.RefResolver('file://' + dir_path + '/schema/', dir_schema)
dir_schema_validator = Draft4Validator(dir_schema, resolver=dir_schema_resolver)


def updateDirHandler(id):

    inputs = request.get_json()

    try:
        dir_schema_validator.validate(inputs)
    except jsonschema.ValidationError as e:
        return jsonify(errors="bad request body: %s" % e.message), 400

    dir_key = current_app.config['dbkeys']['dir']
    dir_capnp_schema = current_app.config['capnp']['dir']

    # create capnp directory object
    dir_capnp = dir_capnp_schema.new_message(**inputs)

    # save new user into kvs
    redis = current_app.config['redis']
    redis.hset(dir_key, str(dir_capnp.uid), dir_capnp.to_bytes_packed())

    return jsonify(dir_capnp.to_dict()), 200, {"Content-type": "application/json"}
