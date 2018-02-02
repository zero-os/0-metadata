# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, request

import json as JSON
import jsonschema
from jsonschema import Draft4Validator

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
group_schema = JSON.load(open(dir_path + '/schema/group_schema.json'))
group_schema_resolver = jsonschema.RefResolver('file://' + dir_path + '/schema/', group_schema)
group_schema_validator = Draft4Validator(group_schema, resolver=group_schema_resolver)


def updateGroupHandler(id):

    inputs = request.get_json()

    try:
        group_schema_validator.validate(inputs)
    except jsonschema.ValidationError as e:
        return jsonify(errors="bad request body"), 400

    return jsonify()
