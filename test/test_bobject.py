#!/usr/bin/python

import unittest
import random
import json
import requests

from client import Client
from client.bobject import bobject as tClass
from .test_base import TestBase
from .equality import bobjectEqual as equal

CLASS='bobject'
URLCLASS='/' + CLASS + '/%s'

class BobjectTests(TestBase):

    def test_create_update_delete(self):

        # Create a object instance
        rand = random.randint(1000, 10000)
        instCreate =  tClass.create(        # ******
            author = 2,
            compressionType = "snappy",
            data = "empty",
            digitalmeUrl = "http://itsyouonline.com",
            domain = 7,
            id = rand,
            key = "secret",
            moddate = 2173,
            signature = "52bb85c0df34f9364d16e5105931647fd3204675",
            uid = rand )

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
        instGet.data = "some data"
        instGet.key = "clearance"
        instGet.signature = "3d02c050bd54dc4aba345466168bb20f84e1a46e"
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
