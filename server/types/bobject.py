# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

"""
Auto-generated class for bobject
"""
from .EnumBobjectCompressionType import EnumBobjectCompressionType
from six import string_types

from . import client_support


class bobject(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type author: int
        :type compressionType: EnumBobjectCompressionType
        :type data: string_types
        :type digitalmeUrl: string_types
        :type domain: int
        :type id: int
        :type key: string_types
        :type moddate: int
        :type signature: string_types
        :type uid: int
        :rtype: bobject
        """

        return bobject(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'bobject'
        data = json or kwargs

        # set attributes
        data_types = [int]
        self.author = client_support.set_property('author', data, data_types, False, [], False, True, class_name)
        data_types = [EnumBobjectCompressionType]
        self.compressionType = client_support.set_property(
            'compressionType', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.data = client_support.set_property('data', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.digitalmeUrl = client_support.set_property(
            'digitalmeUrl', data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.domain = client_support.set_property('domain', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.id = client_support.set_property('id', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.key = client_support.set_property('key', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.moddate = client_support.set_property('moddate', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.signature = client_support.set_property('signature', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.uid = client_support.set_property('uid', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
