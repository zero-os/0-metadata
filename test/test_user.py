#!/usr/bin/python

import unittest
import random
import json
import requests

from client import Client
from client.user import user as UserClass
from .test_base import TestBase
from .equality import userEqual as equal

class UserTests(TestBase):

    def test_create_update_delete(self):

        # Create a user
        rand = random.randint(1000, 10000)
        uc = UserClass.create(addr='home', alias=['jsmith'], keyPub=['123'], uid=rand)
        resp = self.app.post('/user/%s' % uc.uid, data=uc.as_json(), content_type='application/json')
        assert resp.status_code == 200

        # List users: validate if user can be found
        resp = self.app.get('/user')
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code)
        users = _users_factory(resp)
        assert len(users) == 1
        u = users[0]
        assert equal(uc,  u)

        # Retrieve the user
        resp = self.app.get('/user/%s' % uc.uid)
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code)
        user = UserClass.create(**json.loads(resp.data.decode()))
        assert equal(uc,  user)

        # # Update the user
        user.addr = "Work"
        user.alias = ["jdoe"]
        user.keyPub = ["321"]
        resp = self.app.post('/user/%s' % user.uid, data=user.as_json(), content_type='application/json')

        # Check the updated user
        resp = self.app.get('/user/%s' % user.uid)
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code)
        newser = UserClass.create(**json.loads(resp.data.decode()))
        assert equal(newser,  user)

        # Delete User
        resp = self.app.delete('/user/%s' % uc.uid)
        assert resp.status_code == 204, "Unexpected response {}" % (resp.status_code)

        resp = self.app.get('/user/%s' % uc.uid)
        assert resp.status_code == 404


def _users_factory(resp):
    data = resp.get_data()
    if data:
        data = data.decode()
    data = json.loads(data)
    users = []
    for x in data:
        user = UserClass.create(**x)
        users.append(user)
    return users
