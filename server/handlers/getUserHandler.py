# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, current_app
# from .schemas import USERS_KEY, user_schema

from js9 import j
user_schema = j.data.capnp.getSchemaFromPath('capnp/User.capnp', 'User')
USERS_KEY = 'users'

def getUserHandler(id):

    # get capnp encoded users list
    redis = current_app.config['redis']
    user_blob = redis.hget(USERS_KEY, id)
    if user_blob is None: return "", 404

    user = user_schema.from_bytes_packed(user_blob)
    return jsonify(user.to_dict()), 200
