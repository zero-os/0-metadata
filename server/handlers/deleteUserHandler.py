# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, request, current_app

from js9 import j

user_schema = j.data.capnp.getSchemaFromPath('capnp/User.capnp', 'User')

USERS_KEY = 'users'

def deleteUserHandler(id):
    redis = current_app.config['redis']    
    if redis.hdel(USERS_KEY, id) == 1:
        return jsonify(), 204, {"Content-type":"application/json"}
    else:
        return "", 404
