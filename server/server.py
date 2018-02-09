#!/usr/bin/python3
"""
Zero os meta data server
"""

import capnp
import os


def _run():
    # Parse arguments
    import argparse
    parser = argparse.ArgumentParser(description="Zero os meta data server")
    parser.add_argument("host", type=str, help="Webserver host")
    parser.add_argument("port", type=int, help="Webserver port")
    parser.add_argument("redis_host", type=str, help="Redis server host")
    parser.add_argument("redis_port", type=int, help="Redis server port")
    parser.add_argument('--debug', type=bool, default=False, help="Run server in debug mode")
    args = parser.parse_args()

    # connect to redis
    from js9 import j
    redis = j.clients.redis.get(ipaddr=args.redis_host, port=args.redis_port)

    # add redis to app config
    from app import app
    app.config['redis'] = redis

    # Keys used in redis for different types
    app.config['dbkeys'] = _set_db_keys()
    # capnp schemas used to serialize type into database
    app.config['capnp'] = _load_capnp_schemas()

    # run the rest server
    app.run(debug=args.debug, port=args.port, host=args.host)


def _set_db_keys():
    return {
        'user': 'users',
        'dir': 'dir',
        'group': 'group',
        'acl': 'acl',
        'bdomain': 'bdomain',
        'bobject': 'bobject',

    }


def _load_capnp_schemas():
    dir_path = os.path.dirname(__file__)
    return {
        'user': capnp.load(os.path.join(dir_path, 'capnp/User.capnp')).User,
        'dir': capnp.load(os.path.join(dir_path, 'capnp/Dir.capnp')).Dir,
        'group': capnp.load(os.path.join(dir_path, 'capnp/Group.capnp')).Group,
        'acl': capnp.load(os.path.join(dir_path, 'capnp/Acl.capnp')).Acl,
        'bdomain': capnp.load(os.path.join(dir_path, 'capnp/Bdomain.capnp')).Bdomain,
        'bobject': capnp.load(os.path.join(dir_path, 'capnp/Bobject.capnp')).Bobject,
        # 'link': capnp.load('capnp/Dir.capnp').Link
    }


if __name__ == "__main__":
    _run()
