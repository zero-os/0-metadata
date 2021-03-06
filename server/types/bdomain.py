# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

"""
Auto-generated class for bdomain
"""
from six import string_types

from . import client_support


class bdomain(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type addr: string_types
        :type admins: int
        :type author: int
        :type description: string_types
        :type id: int
        :type moddate: int
        :type name: string_types
        :type signature: string_types
        :type uid: int
        :rtype: bdomain
        """

        return bdomain(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'bdomain'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.addr = client_support.set_property('addr', data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.admins = client_support.set_property('admins', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.author = client_support.set_property('author', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.description = client_support.set_property(
            'description', data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.id = client_support.set_property('id', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.moddate = client_support.set_property('moddate', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.name = client_support.set_property('name', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.signature = client_support.set_property('signature', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.uid = client_support.set_property('uid', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
