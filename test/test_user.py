#!/usr/bin/python

import unittest
import random
import logging
import json
import requests

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
        _, resp = self.client.user.updateUser(id=str(rand), data=uc)
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code) 

        # List users: validate if user can be found
        users, resp = self.client.user.listUser() 
        # logging.info("list: %s ", users.content)
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code) 

        for u in users: 
            logging.info("testing %s and %s", rand,u.uid )
            if u.uid == rand:
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
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code) 
        self.assertEqual(newser.addr, 'Work')
        self.assertEqual(newser.alias, ['ryd'])
        self.assertEqual(newser.keyPub, ['321'])
        self.assertEqual(newser.uid, rand)
        
        # Delete User
        resp = self.client.user.deleteUser(id=str(rand))
        assert resp.status_code == 204, "Unexpected response {}" % (resp.status_code) 

        with self.assertRaises(requests.exceptions.HTTPError, msg='should  return 404') as err:
            _ , resp  = self.client.user.getUser(id=str(rand))
  
        