# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, current_app
# from .schemas import USERS_KEY, user_schema

from js9 import j
user_schema = j.data.capnp.getSchemaFromPath('capnp/User.capnp', 'User')
USERS_KEY = 'users'

def listUserHandler():    
    # get capnp encoded users list
    redis = current_app.config['redis']    
    users_blob = redis.hgetall(USERS_KEY)

    response = list()

    for user_blob in users_blob.values():
        user = user_schema.from_bytes_packed(user_blob)
        response.append(user.to_dict())

    return jsonify(response)
