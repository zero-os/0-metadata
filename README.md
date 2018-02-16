# 0-metadata
[![Build Status](https://travis-ci.org/zero-os/0-metadata.svg?branch=master)](https://travis-ci.org/zero-os/0-metadata) [![codecov](https://codecov.io/gh/zero-os/0-metadata/branch/master/graph/badge.svg)](https://codecov.io/gh/zero-os/0-metadata)


0-metadata is a directory management application for keeping track of files stored elsewhere [0-stor](https://github.com/zero-os/0-stor)

Also has a connection to work with the threefold virtual cloud and cryptocurrency.

The project provides with a server and a client, the server makes simple to share a directory among multiple clients, and the client let you access your directory structure from multiple locations or applications.


## Instalation

You need to clone this repository
```
git clone https://github.com/zero-os/0-metadata.git
```

And also you need a redis compatible database, usually we go with [ARDB](https://github.com/yinqiwen/ardb)


## Starting 

The server provides with a REST API, so any http client can operate on the directory, it only needs a redis compatible database to work.

The server only needs a listen address and the database address, so to start it:
```
python3 server.py [-h] [--debug true] host port redis_host redis_port

ie: python3 server.py 0.0.0.0 5000 localhost 6379
```

* --debug, lets you run the server is debug mode

## Documentation

Additional documentation can be found on [DOC](https://github.com/zero-os/0-metadata/doc/Documentation.md)

## Example

Given a 0-metadata server started on vfs.mycompany.com:5000 we can 

* Python3, this code creates a directory and stores it 
```python
#! /usr/bin/python3

from client import Client
from client.dir import dir as Dir
from client.posix import posix as PosixClass

# instanciate client
cl = Client(base_uri="http://vfs.mycompany.com:5000")

# create dir object
my_dir = Dir.create(
    name="home", 
    subdirs=[], 
    uid=1, 
    uidParent=0, 
    size=1, 
    acl=1,
    bobjectItems=[],
    files=[],
    linkItems=[],
    metadataItems=[],
    specialItems=[],
    secret="",
    posix=PosixClass.create(mode=777, uname="root", gname="root"))

data, resp = cl.dir.updateDir(data=my_dir.as_json(), id=str(my_dir.uid))
if resp.status_code != 200:
    print("Returns error: ", resp.status_code)
    exit

print("Success, dir stored: ", data)
```


* Shell Access, this bash code retrieves the directory previously created, you can obtain the same result just using your browser and going to "http://vfs.mycompany.com:5000/dir/1"
```json
$ GET  "http://vfs.mycompany.com:5000/dir/1" 
{
  "acl": 1, 
  "bobjectItems": [], 
  "files": [], 
  "linkItems": [], 
  "metadataItems": [], 
  "name": "home", 
  "posix": {
    "gname": "root", 
    "mode": 777, 
    "uname": "root"
  }, 
  "secret": "", 
  "size": 1, 
  "specialItems": [], 
  "subdirs": [], 
  "uid": 1, 
  "uidParent": 0
}
```
