#!/usr/bin/python

import unittest
import random
import json
import requests
import posix 

from client import Client
from client.dir import dir as tClass
from client.posix import posix as PosixClass
from .test_base import TestBase
from .equality import dirEqual as equal

CLASS='dir'
URLCLASS='/' + CLASS + '/%s'

class DirTests(TestBase):

    def test_create_update_delete(self):

        # Create a object instance
        rand = random.randint(1000, 10000)
        instCreate =  tClass.create(        # ******
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

        resp = self.app.post(URLCLASS % instCreate.uid, data=instCreate.as_json(), content_type='application/json')
        assert resp.status_code == 200

        # List Object: validate if obj can be found
        resp = self.app.get('/' + CLASS)      
        assert resp.status_code == 200
        instances = _class_factory(resp)   
        assert len(instances) == 1
        instList = instances[0]
        assert equal(instCreate, instList)

        # Retrieve the Object
        resp = self.app.get(URLCLASS % instCreate.uid)     
        assert resp.status_code == 200
        instGet = tClass.create(**json.loads(resp.data.decode()))
        assert equal(instCreate, instGet)

        # Update the object
        instGet.name = "another dir name"
        instGet.secret = "FYO"
        instGet.size = 4321
        resp = self.app.post(URLCLASS % instGet.uid, data=instGet.as_json(), content_type='application/json')

        # Check the updated object
        resp = self.app.get(URLCLASS % instGet.uid)
        assert resp.status_code == 200
        instUpd = tClass.create(**json.loads(resp.data.decode())) 
        assert equal(instUpd, instGet)
        
        # Delete object
        resp = self.app.delete(URLCLASS % instCreate.uid)   
        assert resp.status_code == 204, "Unexpected response {}" % (resp.status_code) 

        resp = self.app.get(URLCLASS % instCreate.uid)
        assert resp.status_code == 404


def _class_factory(resp):
    data = resp.get_data()
    if data:
        data = data.decode()

    return [tClass.create(**x) for x in json.loads(data)]        
