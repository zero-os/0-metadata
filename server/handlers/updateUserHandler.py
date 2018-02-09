# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

import json as JSON
import os

import jsonschema
from jsonschema import Draft4Validator

from flask import current_app, jsonify, request


dir_path = os.path.dirname(os.path.realpath(__file__))
user_jschema = JSON.load(open(dir_path + '/schema/user_schema.json'))
user_schema_resolver = jsonschema.RefResolver('file://' + dir_path + '/schema/', user_jschema)
user_schema_validator = Draft4Validator(user_jschema, resolver=user_schema_resolver)


def updateUserHandler(id):
    inputs = request.get_json()
    user_key = current_app.config['dbkeys']['user']
    user_schema = current_app.config['capnp']['user']

    try:
        user_schema_validator.validate(inputs)
    except jsonschema.ValidationError as e:
        return jsonify(errors="bad request body: %s" % e.message), 400

    # create capnp user object
    user_capnp = user_schema.new_message(**inputs)

    # save new user into kvs
    redis = current_app.config['redis']
    redis.hset(user_key, str(user_capnp.uid), user_capnp.to_bytes_packed())

    return jsonify(user_capnp.to_dict()), 200, {"Content-type": 'application/json'}
