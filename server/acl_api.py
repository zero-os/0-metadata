# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

from flask import Blueprint
try:
    from . import handlers
except:
    import handlers


acl_api = Blueprint('acl_api', __name__)


@acl_api.route('/acl', methods=['GET'])
def listAcl():
    """
    Get a list of acls
    It is handler for GET /acl
    """
    return handlers.listAclHandler()


@acl_api.route('/acl/<id>', methods=['GET'])
def getAcl(id):
    """
    Get acl, id=int
    It is handler for GET /acl/<id>
    """
    return handlers.getAclHandler(id)


@acl_api.route('/acl/<id>', methods=['POST'])
def updateAcl(id):
    """
    Update acl
    It is handler for POST /acl/<id>
    """
    return handlers.updateAclHandler(id)


@acl_api.route('/acl/<id>', methods=['DELETE'])
def deleteAcl(id):
    """
    Delete acl
    It is handler for DELETE /acl/<id>
    """
    return handlers.deleteAclHandler(id)
