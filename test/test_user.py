#!/usr/bin/python

import unittest
import random

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
        if resp.status_code !=200: raise Exception("Unexpected response {}" % (resp.status_code) )

        # List users: validate if user can be found
        users, resp = self.client.user.listUser()
        if resp.status_code !=200: raise Exception("Unexpected response {}" % (resp.status_code) )
        for u in users:
            print(u.uid, rand)
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
        if resp.status_code !=200: raise Exception("Unexpected response {}" % (resp.status_code) )
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
        if resp.status_code !=200: raise Exception("Unexpected response {}" % (resp.status_code) )
        self.assertEqual(newser.addr, 'Work')
        self.assertEqual(newser.alias, ['ryd'])
        self.assertEqual(newser.keyPub, ['321'])
        self.assertEqual(newser.uid, rand)
        
        # Delete User
        _, resp = self.client.user.deleteUser(id=str(rand))
        if resp.status_code != 200: raise Exception("Unexpected response {}" % (resp.status_code) )

        _ , resp  = self.client.user.getUser(id=str(rand))
        if resp.status_code != 403: raise Exception("Unexpected response {}" % (resp.status_code) )
        
        