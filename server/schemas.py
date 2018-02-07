import capnp

DIR_KEY = "dir"
USERS_KEY = 'users'

dir_schema = capnp.load('capnp/Dir.capnp').Dir.new_message()
user_schema = capnp.load('capnp/User.capnp').User.new_message()

