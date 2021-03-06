# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

"""
Auto-generated class for acl
"""
from .aci import aci
from six import string_types

from . import client_support


class acl(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type aci: list[aci]
        :type hash: string_types
        :type uid: int
        :rtype: acl
        """

        return acl(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'acl'
        data = json or kwargs

        # set attributes
        data_types = [aci]
        self.aci = client_support.set_property('aci', data, data_types, False, [], True, True, class_name)
        data_types = [string_types]
        self.hash = client_support.set_property('hash', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.uid = client_support.set_property('uid', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
