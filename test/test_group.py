#!/usr/bin/python

import unittest
import random
import json
import requests

from client import Client
from client.group import group as tClass
from .test_base import TestBase
from .equality import groupEqual as equal

CLASS='group'
URLCLASS='/' + CLASS + '/%s'

class GroupTests(TestBase):

    def test_create_update_delete(self):


        # Create instance
        rand = random.randint(1000, 10000)
        instc = tClass.create(addr='home', alias=['jsmith'], keyPub=['123'], uid=rand, owners=7)
        resp = self.app.post('/group/%s' % instc.uid, data=instc.as_json(), content_type='application/json')
        assert resp.status_code == 200

        # List instances: validate if instance can be found
        resp = self.app.get('/' + CLASS)
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code)
        insts = _class_factory(resp)
        assert len(insts) == 1
        i = insts[0]
        assert equal(instc, i)

        # Retrieve the instance
        resp = self.app.get(URLCLASS % instc.uid)
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code)
        inst = tClass.create(**json.loads(resp.data.decode()))
        assert equal(instc, inst) 

        # # Update the instance
        inst.addr = "Work"
        inst.alias = ["jdoe"]
        inst.keyPub = ["321"]
        resp = self.app.post(URLCLASS % inst.uid, data=inst.as_json(), content_type='application/json')

        # Check the updated instance
        resp = self.app.get(URLCLASS % inst.uid)
        assert resp.status_code == 200, "Unexpected response {}" % (resp.status_code)
        newinst = tClass.create(**json.loads(resp.data.decode()))
        assert equal(inst, newinst) 

        # Delete instance
        resp = self.app.delete(URLCLASS % instc.uid)
        assert resp.status_code == 204, "Unexpected response {}" % (resp.status_code)

        resp = self.app.get(URLCLASS % instc.uid)
        assert resp.status_code == 404


def _class_factory(resp):
    data = resp.get_data()
    if data:
        data = data.decode()

    return [tClass.create(**x) for x in json.loads(data)]
