import capnp

DIR_KEY = "dir"
USERS_KEY = 'users'

user_schema = capnp.load('capnp/User.capnp').User
dir_schema = capnp.load('capnp/Dir.capnp').Dir
