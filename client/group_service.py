# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.
from .group import group
from .unhandled_api_error import UnhandledAPIError
from .unmarshall_error import UnmarshallError


class GroupService:
    def __init__(self, client):
        self.client = client

    def deleteGroup(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        Delete group
        It is method for DELETE /group/{id}
        """
        uri = self.client.base_url + "/group/" + id
        return self.client.delete(uri, None, headers, query_params, content_type)

    def getGroup(self, id, headers=None, query_params=None, content_type="application/json"):
        """
        Get group, id=int
        It is method for GET /group/{id}
        """
        uri = self.client.base_url + "/group/" + id
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return group(resp.json()), resp

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def updateGroup(self, data, id, headers=None, query_params=None, content_type="application/json"):
        """
        Update group
        It is method for POST /group/{id}
        """
        uri = self.client.base_url + "/group/" + id
        resp = self.client.post(uri, data, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                return group(resp.json()), resp

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)

    def listGroup(self, headers=None, query_params=None, content_type="application/json"):
        """
        Get a list of groups
        It is method for GET /group
        """
        uri = self.client.base_url + "/group"
        resp = self.client.get(uri, None, headers, query_params, content_type)
        try:
            if resp.status_code == 200:
                resps = []
                for elem in resp.json():
                    resps.append(group(elem))
                return resps, resp

            message = 'unknown status code={}'.format(resp.status_code)
            raise UnhandledAPIError(response=resp, code=resp.status_code,
                                    message=message)
        except ValueError as msg:
            raise UnmarshallError(resp, msg)
        except UnhandledAPIError as uae:
            raise uae
        except Exception as e:
            raise UnmarshallError(resp, e.message)
