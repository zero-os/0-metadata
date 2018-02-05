# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

"""
Auto-generated class for dir
"""
from .link import link
from .link_bobject import link_bobject
from .metadata import metadata
from .posix import posix
from .special import special
from six import string_types

from . import client_support


class dir(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type acl: int
        :type bobject_items: list[link_bobject]
        :type files: list[file]
        :type link_items: list[link]
        :type metadata_items: list[metadata]
        :type name: string_types
        :type posix: posix
        :type secret: string_types
        :type size: int
        :type special_items: list[special]
        :type subdirs: list[link]
        :type uid: int
        :type uid_parent: int
        :rtype: dir
        """

        return dir(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'dir'
        data = json or kwargs

        # set attributes
        data_types = [int]
        self.acl = client_support.set_property('acl', data, data_types, False, [], False, True, class_name)
        data_types = [link_bobject]
        self.bobject_items = client_support.set_property(
            'bobject_items', data, data_types, False, [], True, True, class_name)
        data_types = [file]
        self.files = client_support.set_property('files', data, data_types, False, [], True, True, class_name)
        data_types = [link]
        self.link_items = client_support.set_property('link_items', data, data_types, False, [], True, True, class_name)
        data_types = [metadata]
        self.metadata_items = client_support.set_property(
            'metadata_items', data, data_types, False, [], True, True, class_name)
        data_types = [string_types]
        self.name = client_support.set_property('name', data, data_types, False, [], False, True, class_name)
        data_types = [posix]
        self.posix = client_support.set_property('posix', data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.secret = client_support.set_property('secret', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.size = client_support.set_property('size', data, data_types, False, [], False, True, class_name)
        data_types = [special]
        self.special_items = client_support.set_property(
            'special_items', data, data_types, False, [], True, True, class_name)
        data_types = [link]
        self.subdirs = client_support.set_property('subdirs', data, data_types, False, [], True, True, class_name)
        data_types = [int]
        self.uid = client_support.set_property('uid', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.uid_parent = client_support.set_property(
            'uid_parent', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)