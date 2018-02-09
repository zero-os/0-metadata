#!/usr/bin/python3
"""
Zero os meta data server
"""

import capnp


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
    app.config['dbkeys'] = {
        'user': 'users',
        'dir': 'dir',
    }
    # capnp schemas used to serialize type into database
    app.config['capnp'] = _load_capnp_schemas()

    # run the rest server
    app.run(debug=args.debug, port=args.port, host=args.host)


def _load_capnp_schemas():
    return {
        'user': capnp.load('capnp/User.capnp').User,
        'dir': capnp.load('capnp/Dir.capnp').Dir
    }


if __name__ == "__main__":
    _run()
