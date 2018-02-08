# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, request, current_app

import json as JSON
import jsonschema
from jsonschema import Draft4Validator

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_schema = JSON.load(open(dir_path + '/schema/dir_schema.json'))
dir_schema_resolver = jsonschema.RefResolver('file://' + dir_path + '/schema/', dir_schema)
dir_schema_validator = Draft4Validator(dir_schema, resolver=dir_schema_resolver)

from .schemas import DIR_KEY, dir_schema


def updateDirHandler(id):
    inputs = request.get_json()

    try:
        dir_schema_validator.validate(inputs)
    except jsonschema.ValidationError as e:
        return jsonify(errors="bad request body: %s" % e.message), 400

    # create capnp directory object
    dir_capnp = dir_schema.new_message(**inputs)

    # save new user into kvs
    redis = current_app.config['redis']
    redis.hset(DIR_KEY, str(dir_capnp.uid), dir_capnp.to_bytes_packed())

    return inputs
