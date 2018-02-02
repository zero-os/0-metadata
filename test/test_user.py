#!/usr/bin/python
import unittest
from client import Client
from client.user import user

class UserTests(unittest.TestCase):

    def setUp(self):
        self.client = Client(base_uri="http://localhost:8888")


    def test_create_update(self):
        # Create a user
        uc = user.create(addr='home', alias=['enric'], keyPub=['123'], uid=2)
        self.client.user.updateUser(id=str(2), data=uc)

        # List users: validate if user can be found
        users, _ = self.client.user.listUser()
        for u in users:
            if u.uid == 2:
                self.assertEqual(u.addr, 'home')
                self.assertEqual(u.alias, ['enric'])
                self.assertEqual(u.keyPub, ['123'])
                self.assertEqual(u.uid, 2)
                break
        else:
            raise Exception("User not found!")

        # Update the user

        # List users: validate if user can be found