# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, request, current_app
from schemas import USERS_KEY, user_factory

user_schema = user_factory()

def deleteUserHandler(id):
    redis = current_app.config['redis']    
    if redis.hdel(USERS_KEY, id) == 1:
        return jsonify(), 204, {"Content-type":"application/json"}
    else:
        return "", 404
