import capnp

DIR_KEY = "dir"
USERS_KEY = 'users'


# Object factories Returns a new object message every time they are called

def user_factory()
    return capnp.load('capnp/Dir.capnp').Dir.new_message()

def dir_factory()    
    return capnp.load('capnp/User.capnp').User.new_message()

