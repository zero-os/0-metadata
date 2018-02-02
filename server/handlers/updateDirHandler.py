# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

from flask import jsonify, request

import json as JSON
import jsonschema
from jsonschema import Draft4Validator

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_schema = JSON.load(open(dir_path + '/schema/dir_schema.json'))
dir_schema_resolver = jsonschema.RefResolver('file://' + dir_path + '/schema/', dir_schema)
dir_schema_validator = Draft4Validator(dir_schema, resolver=dir_schema_resolver)


def updateDirHandler(id):

    inputs = request.get_json()

    try:
        dir_schema_validator.validate(inputs)
    except jsonschema.ValidationError as e:
        return jsonify(errors="bad request body"), 400

    return jsonify()
