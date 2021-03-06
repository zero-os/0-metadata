# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

"""
Auto-generated class for group
"""
from six import string_types

from . import client_support


class group(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type addr: string_types
        :type alias: list[string_types]
        :type keyPub: list[string_types]
        :type owners: int
        :type uid: int
        :rtype: group
        """

        return group(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'group'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.addr = client_support.set_property('addr', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.alias = client_support.set_property('alias', data, data_types, False, [], True, True, class_name)
        data_types = [string_types]
        self.keyPub = client_support.set_property('keyPub', data, data_types, False, [], True, False, class_name)
        data_types = [int]
        self.owners = client_support.set_property('owners', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.uid = client_support.set_property('uid', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
