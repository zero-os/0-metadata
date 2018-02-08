# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, request, current_app
import json as JSON
import jsonschema
from jsonschema import Draft4Validator
# from .schemas import USERS_KEY, user_schema

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
user_jschema = JSON.load(open(dir_path + '/schema/user_schema.json'))
user_schema_resolver = jsonschema.RefResolver('file://' + dir_path + '/schema/', user_jschema)
user_schema_validator = Draft4Validator(user_jschema, resolver=user_schema_resolver)


from js9 import j
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
    redis.hset(USERS_KEY, str(user_capnp.uid), user_capnp.to_bytes_packed())

    return jsonify(user_capnp.to_dict())
