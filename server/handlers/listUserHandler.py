# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, request, current_app
from js9 import j
import logging

user_schema = j.data.capnp.getSchemaFromPath('capnp/User.capnp', 'User')

USERS_KEY = 'users'


def listUserHandler():

    # get capnp encoded users list
    redis = current_app.config['redis']    
    users_blob = redis.hgetall(USERS_KEY)

    response = list()

    for user_blob in users_blob.values():
        try:
            user = user_schema.from_bytes_packed(user_blob)
        except:
            # Added because this happened to me, but the condition needs to be clearer
            logging.warn(msg="Corrupted DB@'users' : skipping user")
            continue 

        response.append(user.to_dict())

    return jsonify(response)
