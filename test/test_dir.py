#!/usr/bin/python

import unittest
import random
import logging
import json
import requests

from client import Client
from client.dir import dir as DirClass

class UserTests(unittest.TestCase):

    def setUp(self):
        self.client = Client(base_uri="http://localhost:8888")


    def test_create_update_delete(self):

        # Create a object instance
        rand = random.randint(1000, 10000)
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

        # Update the object
        inst.addr = "Work"          # ******
        inst.alias = ["ryd"]        # ******
        inst.keyPub = ["321"]       # ******
        self.client.dir.updateDir(id=str(rand), data=inst)  # ******
        
        # Check the updated object
        newinst, resp = self.client.dir.getUser(id=str(rand))   # ******
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code) 
        self.assertEqual(newinst.addr, 'Work')      # ******
        self.assertEqual(newinst.alias, ['ryd'])    # ******
        self.assertEqual(newinst.keyPub, ['321'])   # ******
        self.assertEqual(newinst.uid, rand)         # ******
        
        # Delete object
        resp = self.client.dir.deleteDir(id=str(rand))  # ******
        assert resp.status_code == 204, "Unexpected response {}" % (resp.status_code) 

        with self.assertRaises(requests.exceptions.HTTPError, msg='should  return 404') as err:
            _ , resp  = self.client.dir.getDir(id=str(rand))    # ******
  
        