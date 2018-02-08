import capnp
import os
DIR_KEY = "dir"
USERS_KEY = 'users'


# Object factories Returns a new object message every time they are called
base_path = os.path.dirname(__file__)
dir_schema = capnp.load(os.path.join(base_path, 'capnp/Dir.capnp')).Dir
user_schema = capnp.load(os.path.join(base_path, 'capnp/User.capnp')).User
