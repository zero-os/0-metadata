# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

from flask import Blueprint
import handlers


group_api = Blueprint('group_api', __name__)


@group_api.route('/group', methods=['GET'])
def listGroup():
    """
    Get a list of groups
    It is handler for GET /group
    """
    return handlers.listGroupHandler()


@group_api.route('/group/<id>', methods=['GET'])
def getGroup(id):
    """
    Get group, id=int
    It is handler for GET /group/<id>
    """
    return handlers.getGroupHandler(id)


@group_api.route('/group/<id>', methods=['POST'])
def updateGroup(id):
    """
    Update group
    It is handler for POST /group/<id>
    """
    return handlers.updateGroupHandler(id)


@group_api.route('/group/<id>', methods=['DELETE'])
def deleteGroup(id):
    """
    Delete group
    It is handler for DELETE /group/<id>
    """
    return handlers.deleteGroupHandler(id)