import capnp

DIR_KEY = "dir"
USERS_KEY = 'users'


# Object factories Returns a new object message every time they are called

dir_schema = capnp.load('capnp/Dir.capnp').Dir
user_schema = capnp.load('capnp/User.capnp').User

def user_factory()
    return user_schema.new_message()

def dir_factory()    
    return dir_schema.new_message()

