#0-metadata

This project goal is to create a personal generic metadata stor.
It will integrate in the 0-OS ecosystem as the goto place to store metadata.

The organization of the metadata will be done in a directory structure. 
This has been chosen cause this is a structure people know and it also allow to be efficient in term of storage space.

## Technical
The 0-metadata server is going to expose an REST API generated with [go-raml](https://github.com/Jumpscale/go-raml).
This API will let user manage files and directories. The directories will be serialized into a capnp structure and stored into a key-value store. 
This concept has been proven to allow fast listing and access to the files (this is what we use for [0-fs](https://github.com/zero-os/0-fs) and flist).

Key-valu store used: To be choosen.

Definitions of the types used: see [raml specification](main.raml)