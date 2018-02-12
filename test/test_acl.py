#!/usr/bin/python

import unittest
import random
import json
import requests
import posix 

from client import Client
from client.acl import acl as tClass
from .test_base import TestBase
from .equality import aclEqual as equal

CLASS='acl'
URLCLASS='/' + CLASS + '/%s'

class DirTests(TestBase):

    def test_create_update_delete(self):

        # Create a object instance
        rand = random.randint(1000, 10000)
        instCreate =  tClass.create(        # ******
            aci = [], hash = "code hash", uid = rand )

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
        instGet.hash = "another hash codec"           # *****
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

