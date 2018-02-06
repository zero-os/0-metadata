# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, request, current_app

from js9 import j

user_schema = j.data.capnp.getSchemaFromPath('capnp/User.capnp', 'User')

USERS_KEY = 'users'

def getUserHandler(id):

    # get capnp encoded users list
    redis = current_app.config['redis']
    user_blob = redis.hget(USERS_KEY, id)
    try:    
        user = user_schema.from_bytes_packed(user_blob)    
    except:
        # We return 404 because is the normal, but as with listUderHandler could be a corrupted database too
        return "", 404

    return jsonify(user.to_dict()), 200
