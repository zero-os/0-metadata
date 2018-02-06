# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

import logging
from flask import jsonify, request, current_app

from js9 import j

user_schema = j.data.capnp.getSchemaFromPath('capnp/User.capnp', 'User')

logger = logging.getLogger(__name__)

USERS_KEY = 'users'

def deleteUserHandler(id):

    logger.info("DeleteUserHandler ", id)

    redis = current_app.config['redis']    
    if redis.hdel(USERS_KEY, id) == 1:
        return jsonify(), 204, {"Content-type":"application/json"}
    else:
        return "", 404
