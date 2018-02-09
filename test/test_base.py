import unittest
from server.app import app
from server.server import _load_capnp_schemas, _set_db_keys
import fakeredis


class TestBase(unittest.TestCase):

    def setUp(self):
        app.config['redis'] = fakeredis.FakeRedis()
        app.testing = True

        # Keys used in redis for different types
        app.config['dbkeys'] = _set_db_keys()
        # capnp schemas used to serialize type into database
        app.config['capnp'] = _load_capnp_schemas()

        # capnp schemas used to serialize type into database
        app.config['capnp'] = _load_capnp_schemas()
        self.app = app.test_client()

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
