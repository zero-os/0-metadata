# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, request, current_app

import json as JSON
import jsonschema
from jsonschema import Draft4Validator


from js9 import j


import os

dir_path = os.path.dirname(os.path.realpath(__file__))
user_schema = JSON.load(open(dir_path + '/schema/user_schema.json'))
user_schema_resolver = jsonschema.RefResolver('file://' + dir_path + '/schema/', user_schema)
user_schema_validator = Draft4Validator(user_schema, resolver=user_schema_resolver)

user_schema = j.data.capnp.getSchemaFromPath('capnp/User.capnp', 'User')


USERS_KEY = 'users'


def updateUserHandler(id):

    inputs = request.get_json()

    try:
        user_schema_validator.validate(inputs)
    except jsonschema.ValidationError as e:
        return jsonify(errors="bad request body: %s" % e.message), 400

    # create capnp user object
    user_capnp = user_schema.from_dict(inputs)

    # save new user into kvs
    redis = current_app.config['redis']
    num = redis.hset(USERS_KEY, str(user_capnp.uid), user_capnp.to_bytes_packed())
    if num == 0:
        return "ID Already exists, can not update", 403 # ID Already Exists, will not update

    return jsonify(user_capnp.to_dict())
