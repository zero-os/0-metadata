# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, request, current_app

from js9 import j

user_schema = j.data.capnp.getSchemaFromPath('capnp/User.capnp', 'User')

USERS_KEY = 'users'

def getUserHandler(id):

    # get capnp encoded users list
    redis = current_app.config['redis']    
    user_blob = redis.hget(USERS_KEY, id)
    user = user_schema.from_bytes_packed(user_blob)
    user.to_dict()

    return jsonify(user.to_dict())
