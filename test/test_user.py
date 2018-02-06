#!/usr/bin/python

import unittest
import random
import logging
import json

from client import Client
from client.user import user as UserClass

class UserTests(unittest.TestCase):

    def setUp(self):
        self.client = Client(base_uri="http://localhost:8888")


    def test_create_update_delete(self):
        # def assignUser (addr, alias, keyPub,)

        # Create a user
        rand = random.randint(1000, 10000)
        uc =  UserClass.create(addr='home', alias=['enric'], keyPub=['123'], uid=rand)
        resp = self.client.user.updateUser(id=str(rand), data=uc)
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code) 

        # List users: validate if user can be found
        users = self.client.user.listUser() #  returns text, older versions of this call returned json
        # logging.info("list: %s ", users.content)
        assert users.status_code == 200, "Unexpected response {}" % (users.status_code) 

        for u in users.json(): # It returns a dictionary, in older version users was a list of user class
            logging.info("testing %s and %s", rand,u['uid'] )
            if u['uid'] == rand:
                self.assertEqual(u.addr, 'home')
                self.assertEqual(u.alias, ['enric'])
                self.assertEqual(u.keyPub, ['123'])
                self.assertEqual(u.uid, rand)
                break
        else:
            raise Exception("User not found!")

        # Retrieve the user
        user, resp = self.client.user.getUser(id=str(rand))
        assert resp.status_code ==200, "Unexpected response {}" % (resp.status_code) 
        self.assertEqual(user.addr, 'home')
        self.assertEqual(user.alias, ['enric'])
        self.assertEqual(user.keyPub, ['123'])
        self.assertEqual(user.uid, rand)

        # Update the user
        user.addr = "Work"
        user.alias = ["ryd"]
        user.keyPub = ["321"]
        self.client.user.updateUser(id=str(rand), data=user)
        
        # Check the updated user
        newser, resp = self.client.user.getUser(id=str(rand))
        assert resp.status_code == 200 "Unexpected response {}" % (resp.status_code) 
        self.assertEqual(newser.addr, 'Work')
        self.assertEqual(newser.alias, ['ryd'])
        self.assertEqual(newser.keyPub, ['321'])
        self.assertEqual(newser.uid, rand)
        
        # Delete User
        resp = self.client.user.deleteUser(id=str(rand))
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code) 

        _ , resp  = self.client.user.getUser(id=str(rand))
        assert resp.status_code == 404, "Unexpected response {}" % (resp.status_code) 
        
        