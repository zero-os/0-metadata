#!/usr/bin/python

import unittest
import random
import logging
import json
import requests
<<<<<<< HEAD
<<<<<<< HEAD

from client import Client
from client.dir import dir as DirClass
=======
from .equality import dirEqual as equal

from client import Client
=======
from .equality import dirEqual as equal

from client import Client
>>>>>>> e07e12d... Some refactoring on User and Dir handlers
from client.dir import dir as tClass
from client.posix import posix as PosixClass
from .test_base import TestBase
import posix 
>>>>>>> e07e12d... Some refactoring on User and Dir handlers

class UserTests(unittest.TestCase):

    def setUp(self):
        self.client = Client(base_uri="http://localhost:8888")


    def test_create_update_delete(self):

        # Create a object instance
        rand = random.randint(1000, 10000)
<<<<<<< HEAD
<<<<<<< HEAD
        inst =  DirClass.create(        # ******
              acl = 2
            , bobject_items = list()
            , files = list()
            , link_items =list()
            , metadata_items = list()
            , name = "directory_name"
            , posix = None
            , secret = "secret"
            , size = 2173
            , special_items = list()
            , subdirs = list() 
            , uid = rand
            , uid_parent = 1 )

        _, resp = self.client.dir.updateDir(id=str(rand), data=inst)    # ******
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code) 

        # List objects: validate if instance can be found
        instList, resp = self.client.dir.listDir() # ******
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code) 

        for inst in instList: 
            logging.info("testing %s and %s", rand,inst.uid )
            if inst.uid == rand:
                self.assertEqual(inst.addr, 'home')         # ******
                self.assertEqual(inst.alias, ['enric'])     # ******
                self.assertEqual(inst.keyPub, ['123'])      # ******
                self.assertEqual(inst.uid, rand)            
                break
        else:
            raise Exception("Dir not found!")       # ******

        # Retrieve the object
        inst, resp = self.client.dir.getDir(id=str(rand))   # ******
        assert resp.status_code ==200, "Unexpected response {}" % (resp.status_code) 
        self.assertEqual(inst.addr, 'home')                 # ******
        self.assertEqual(inst.alias, ['enric'])             # ******
        self.assertEqual(inst.keyPub, ['123'])              # ******
        self.assertEqual(inst.uid, rand)                    
=======
=======
>>>>>>> e07e12d... Some refactoring on User and Dir handlers
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

        resp = self.app.post('/dir/%s' % instCreate.uid, data=instCreate.as_json(), content_type='application/json')
        assert resp.status_code == 200

        # List Object: validate if obj can be found
        resp = self.app.get('/dir')     # ****
        assert resp.status_code == 200
        instances = _class_factory(resp)  # *****
        assert len(instances) == 1
        instList = instances[0]
        assert equal(instCreate, instList)

        # Retrieve the Object
        resp = self.app.get('/dir/%s' % instCreate.uid)     # ******
        assert resp.status_code == 200
        instGet = tClass.create(**json.loads(resp.data.decode()))
        assert equal(instCreate, instGet)
<<<<<<< HEAD
>>>>>>> e07e12d... Some refactoring on User and Dir handlers
=======
>>>>>>> e07e12d... Some refactoring on User and Dir handlers

        # Update the object
        inst.addr = "Work"          # ******
        inst.alias = ["ryd"]        # ******
        inst.keyPub = ["321"]       # ******
        self.client.dir.updateDir(id=str(rand), data=inst)  # ******
        
        # Check the updated object
<<<<<<< HEAD
        newinst, resp = self.client.dir.getUser(id=str(rand))   # ******
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code) 
        self.assertEqual(newinst.addr, 'Work')      # ******
        self.assertEqual(newinst.alias, ['ryd'])    # ******
        self.assertEqual(newinst.keyPub, ['321'])   # ******
        self.assertEqual(newinst.uid, rand)         # ******
=======
        resp = self.app.get('/dir/%s' % instGet.uid)
        assert resp.status_code == 200
        instUpd = tClass.create(**json.loads(resp.data.decode())) 
        assert equal(instUpd, instGet)
<<<<<<< HEAD
>>>>>>> e07e12d... Some refactoring on User and Dir handlers
=======
>>>>>>> e07e12d... Some refactoring on User and Dir handlers
        
        # Delete object
        resp = self.client.dir.deleteDir(id=str(rand))  # ******
        assert resp.status_code == 204, "Unexpected response {}" % (resp.status_code) 

<<<<<<< HEAD
        with self.assertRaises(requests.exceptions.HTTPError, msg='should  return 404') as err:
            _ , resp  = self.client.dir.getDir(id=str(rand))    # ******
  
        
=======
        resp = self.app.get('/dir/%s' % instCreate.uid)
        assert resp.status_code == 404


def _class_factory(resp):
    data = resp.get_data()
    if data:
        data = data.decode()

    return [tClass.create(**x) for x in json.loads(data)]        

>>>>>>> e07e12d... Some refactoring on User and Dir handlers
