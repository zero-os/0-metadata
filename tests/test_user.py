#!/usr/bin/python

import json
import random
import time
import unittest

import requests

from client.user import user as UserClass

from .test_base import TestBase


class UserTests(TestBase):

    def __init__(self, methodName):
        super().__init__(methodName)

    def test_create_update_delete(self):

        # Create a user
        rand = random.randint(1000, 10000)
        uc = UserClass.create(addr='home', alias=['jsmith'], keyPub=['123'], uid=rand)
        _, resp = self.client.user.updateUser(id=str(rand), data=uc)
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code)

        # List users: validate if user can be found
        users, resp = self.client.user.listUser()
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code)
        assert len(users) == 1
        u = users[0]
        assert u.uid == uc.uid
        assert u.addr == 'home'
        assert u.alias == ['jsmith']
        assert u.keyPub == ['123']

        # Retrieve the user
        user, resp = self.client.user.getUser(id=str(rand))
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code)
        assert user.addr == 'home'
        assert user.alias == ['jsmith']
        assert user.keyPub == ['123']
        assert user.uid == rand

        # Update the user
        user.addr = "Work"
        user.alias = ["jdoe"]
        user.keyPub = ["321"]
        self.client.user.updateUser(id=str(rand), data=user)

        # Check the updated user
        newser, resp = self.client.user.getUser(id=str(rand))
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code)
        assert newser.addr == 'Work'
        assert newser.alias == ['jdoe']
        assert newser.keyPub == ['321']
        assert newser.uid == rand

        # Delete User
        resp = self.client.user.deleteUser(id=str(rand))
        assert resp.status_code == 204, "Unexpected response {}" % (resp.status_code)

        with self.assertRaises(requests.exceptions.HTTPError, msg='should  return 404') as err:
            _, resp = self.client.user.getUser(id=str(rand))
