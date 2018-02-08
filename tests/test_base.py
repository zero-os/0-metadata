import os
import signal
import time
import unittest
from multiprocessing import Process

import fakeredis
from client import Client
from server.app import app


def _server():
    app.config['redis'] = fakeredis.FakeStrictRedis()

    # run the rest server
    app.run(debug=True, port=8888, host='localhost')
    print('exit sub proc')


class TestBase(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.client = None

    def setUp(self):
        self.p = Process(target=_server)
        self.p.start()
        print(self.p.pid)
        time.sleep(0.5)

        self.client = Client(base_uri="http://localhost:8888")

    def tearDown(self):
        # self.p.terminate()
        os.kill(self.p.pid, signal.SIGKILL)
        self.p.join()
        print("tearDown")
