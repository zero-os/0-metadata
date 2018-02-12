#!/usr/bin/python

import unittest
import random
import json
import requests

from client import Client
from client.user import user as tClass
from .test_base import TestBase
from .equality import userEqual as equal

CLASS='user'
URLCLASS='/' + CLASS + '/%s'

class UserTests(TestBase):

    def test_create_update_delete(self):

        # Create a user
        rand = random.randint(1000, 10000)
        uc = tClass.create(addr='home', alias=['jsmith'], keyPub=['123'], uid=rand)
        resp = self.app.post(URLCLASS % uc.uid, data=uc.as_json(), content_type='application/json')
        assert resp.status_code == 200

        # List users: validate if user can be found
        resp = self.app.get('/' + CLASS)
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code)
        users = _class_factory(resp)
        assert len(users) == 1
        u = users[0]
        assert equal(uc,  u)

        # Retrieve the user
        resp = self.app.get(URLCLASS % uc.uid)
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code)
        user = tClass.create(**json.loads(resp.data.decode()))
        assert equal(uc,  user)

        # # Update the user
        user.addr = "Work"
        user.alias = ["jdoe"]
        user.keyPub = ["321"]
        resp = self.app.post(URLCLASS % user.uid, data=user.as_json(), content_type='application/json')

        # Check the updated user
        resp = self.app.get(URLCLASS % user.uid)
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code)
        newser = tClass.create(**json.loads(resp.data.decode()))
        assert equal(newser,  user)

        # Delete User
        resp = self.app.delete(URLCLASS % uc.uid)
        assert resp.status_code == 204, "Unexpected response {}" % (resp.status_code)

        resp = self.app.get(URLCLASS % uc.uid)
        assert resp.status_code == 404


def _class_factory(resp):
    data = resp.get_data()
    if data:
        data = data.decode()

    return [tClass.create(**x) for x in json.loads(data)]
