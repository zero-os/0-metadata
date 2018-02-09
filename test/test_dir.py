#!/usr/bin/python

import unittest
import random
import json
import requests
from .equality import dirEqual

from client import Client
from client.dir import dir as DirClass
from client.posix import posix as PosixClass
from .test_base import TestBase
import posix 


class DirTests(TestBase):

    def test_create_update_delete(self):

        # Create a object instance
        rand = random.randint(1000, 10000)
        instCreate =  DirClass.create(        # ******
            acl = 2,
            bobjectItems = [],
            files = [],
            linkItems = [],
            metadataItems = [],
            name = "directory_name",
            posix = PosixClass.create(mode=777, uname="root", gname="root"),
            secret = "secret",
            size = 2173,
            specialItems = [],
            subdirs = [] ,
            uid = rand,
            uidParent = 1 )

        resp = self.app.post('/dir/%s' % instCreate.uid, data=instCreate.as_json(), content_type='application/json')
        assert resp.status_code == 200

        # List Object: validate if obj can be found
        resp = self.app.get('/dir')     # ****
        assert resp.status_code == 200
        instances = _dir_factory(resp)  # *****
        assert len(instances) == 1
        instList = instances[0]
        dirEqual(instCreate, instList)

        # Retrieve the Object
        resp = self.app.get('/dir/%s' % instCreate.uid)     # ******
        assert resp.status_code == 200
        instGet = DirClass.create(**json.loads(resp.data.decode()))
        dirEqual(instCreate, instGet)

        # Update the object
        instGet.name = "another dir name"
        instGet.secret = "FYO"
        instGet.size = 4321
        resp = self.app.post('/dir/%s' % instGet.uid, data=instGet.as_json(), content_type='application/json')

        # Check the updated object
        resp = self.app.get('/dir/%s' % instGet.uid)
        assert resp.status_code == 200
        instUpd = DirClass.create(**json.loads(resp.data.decode())) 
        dirEqual(instUpd, instGet)
        
        # Delete object
        resp = self.app.delete('/dir/%s' % instCreate.uid)  # ******
        assert resp.status_code == 204, "Unexpected response {}" % (resp.status_code) 

        resp = self.app.get('/dir/%s' % instCreate.uid)
        assert resp.status_code == 404


def _dir_factory(resp):
    data = resp.get_data()
    if data:
        data = data.decode()

    return [DirClass.create(**x) for x in json.loads(data)]        

