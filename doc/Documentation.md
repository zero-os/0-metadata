# 0-Metadata 

This document describes the operation and methods available in this API

0-metadata is a filesystem management system unlinked from storage, it let you create, delete, rename... files, dirs ... but has no mass storage asociated to the files. This way it let you manage a filesystem while keeping track of where (if any) the storage keeps the content of the files.

As such it counts with a simple REST interface to the world.

It defines a set of objects, which you may be already familiar with, like dir, file, link ....


## Objects

Every object has a name a type and a desciption, optionally you will found a "!" sign to indicate that this field is optional.


* [Dir](#Dir)
* [Special](#Dir)
* [Link](#Link)
* [File](#File)
* [Metadata](#Metadata)
* [Bdomain](#Bdomain)
* [Bobject](#Bobject)
* [Link_bobject](#Link_bobject)
* [Posix](#Posix)
* [Acl](#Acl)
* [Aci](#Aci)
* [User](#User)
* [Group](#Group)



## Dir
The Dir object keeps track of its structure, the files it contain and access permissions:

It is defined as:
```
uid:int32                   unique ID
uidParent:int32             link to parent of this object
secret:string               secret to share when give someone access to info of full dir obj
name:string                 name of this object
size:int32                  size in bytes of full dir (calculated when mod done on any of sub obj)
files:file[]                list of the file objects
specialItems:special[]      list of the special objects
linkItems:link[]            list of the special objects
metadataItems:metadata[]    list of the metadata objects
bobjectItems:link_bobject[] list of the blockchain objects
subdirs:link[]              link to subdirs of this dir, can use Link obj for this
!posix:posix                posix object if storing files and used for filesystem
acl:int32                   link to acl object to allow someone access or not
```
Most of the fields are self explanatory but among the ones that may require some additional info:

* files: is an array that represents a set of ordinary files
* specialItems: array that represents files in the directory that are kernel interfaces, ie: devices, pipes and sockets
* linkItems: array of the links in the directory, objects that points to another file ie: a link
* metadataItems: array of metadata associated with the blockchain objects
* bobjectItems: array of blockchain objects
* subdir: array of links to other directories which have this one as parent
* posix: keeps permissions to access the directory
* acl: directory permissions using lists, ie: user:group:permission

The Dir object has 2 REST paths:

**/dir**
```
GET: returns all directories on a given 0-metadata api as a json array
POST: updates/creates the directory identified by the uid in the json body of the request
```
**/dir/{id}**
```
GET: returns the directoy who's uid is equal to {id}
POST: same as before, as POST don't look at the {id} just the uid in the body of the request
DELETE: deletes the directory who's uid is {id}
```
Reading and writing directories are large operations that may take time, as responses can become big.

GET /dir is a list operation and can take a lot of time as the number of users can be very large, use with caution.


## Special
The Special object, represents kernel objects that have a file interface, like sockets, devices and named pipes.

It is defined as:
```
name:string     name of this object
type:[ socket, block, char, fifo ] kind of kernel object represented by this object
data:string     data relevant for type of item
moddate:int32   epoch
```
Special objects have no defined interface with the REST API, they are used as part of the Dir object


## Link
The link object is a generic pointer to another object, it is used as an easy to handle abstraction for directories, files and metadata

It is defined as:
```
name:string name of this object
destdir:int32  id to directory where link points too
destname:int32  name of the file or other item in the directory
type:[ file, dir, meta ]  type of destination object
moddate:int32 epoch
```
> Questions: what is destname ? 

Link objects have not a defined interface with the REST API, they are used as part of the Dir object


## File
The File object, keeps the info needed to reference a file on some storage area

It is defined as:
```
name:string  name of this object
size:int32  size in bytes of full file
moddate:int32  epoch
blockSize:int16  size in 4kbytes blocks, same for all parts of file (apart from last one)
blocks:fileblock[] list of the parts of the file
!posix:Posix  posix object if storing files and used for filesystem
```
Files are as most other defined structures, part of the Dir object, it uses fileblock to indicate how the file is composed on the storage area

A fileblock is defined as:
```
!hash:string File hash stored as key on the backend (of the block)
!zstormetadata:string metadata of zstor
!key:string  Encryption key (is optional, if not given then not encrypted)
```

> Question: Why encryption is done on a block basis ? Should the file be encrypted or not, but has no sense to have a block encrypted and the next one without ecnryption

> Question: Why do we let the user manage the blocks? this smells trouble as any mistake on the user part or even on our part will screw the 0-metastor


## Metadata
> Need more knowledge to describe what this is and how it works
```
name:string  name of this bobject, to show in dir
data:string   metadata of zstor
!category:string "category of the metadata, optional"
moddate:int32 epoch
```


## Bdomain
> Need more knowledge to describe what this is and how it works
```
id:int32  increment id for any domain in a blockchain, is stored in itself in bdomain 1 (always)
uid:int32  unique id
moddate:int32  epoch, last modification date
author:int32  id of author who created this bobject
name:string  name of the domain, needs to be unique
!description:string  description as defined by owner of the domain
admins:int32  list of users who administer this domain
!addr:string  address given by the digital.me system, is for the master of this blockchain
signature:string  signature with priv key of author of md5(id+moddate+author+name+signature+owners(sorted)+addr+signature previous message)
```
> Question: Why name needs to be unique ? uid aready are, maybe uid is not needed

**/bdomain**

**/bdomain/{id}**


## Bobject
> Need more knowledge to describe what this is and how it works
```
id:int32   is incremental id for any object in a blockchain, unique for all changes
!uid:int32  is unique id which stays the same even after mods, there needs to be lookup table
key:string  secret or key, can be used to give someone access to data of this obj, max 32 bytes
domain:int32  is unique id for the domain in which this bobject lives e.g. user.system
moddate:int32  last modification date
author:int32  id of author who created this bobject
data:string  the capnp data
signature:string  signature with priv key of author of md5(id+domain+moddate+author+data+signature+signature previous message)
!compressionType:[ none, blosc, snappy ] compression type of the message, default is none
!digitalmeUrl:string  digital.me url
```

**/bobject**

**/bobject/{id}**


## Link_bobject
> Need more knowledge to describe what this is and how it works
```
bdomain:int32  domain id of the blockchain
buid:int32  unique id inside the blockchain domain
name: string   name of this bobject, to show in dir
!secret:string can be used to allow user to fetch the object without authentication
moddate:int32  epoch, last modification date
```

## Posix
> Need more knowledge to describe what this is and how it works
```
mode:int16  posix mode
uname:string posix uname
gname:string posix gname (group)
```

## Acl
> Need more knowledge to describe what this is and how it works
```
uid: int32  is unique id for the acl, increments
aci:aci[]  list of access control items
hash:string  md5 hash of concatenation of ACI hashes, used to find this acl to avoid duplicates
```

**/acl**

**/acl/{id}**


## Aci
```
uid:string  is unique id for the acl, increments
!groups:int32[] link to group(s)
!users:int32[] link to user(s)
right:string  |
    text e.g. rwdl- (admin read write delete list -), freely to be chosen
    admin means all rights (e.g. on / = namespace or filesystem level all rights for everything)
    '-' means remove all previous ones (is to stop recursion), if group=0,user=0 then is for all users & all groups
hash:string  md5 hash of id+sorted_groups+sorted_users+right, used to make sure we only link acl once
```


## User
The user object identifies a unique person

Its defined as:
```
uid:int32 unique ID 
alias:string[] chosen name(s), relevant in groups you belong.
keyPub:string[] public key which is used for validation & encryption
addr:string is the address given by the digital.me system, is unique per user & can change
```
> Question: What happens when the addr change? how does 0-metastor knows about the change?

The User object has 2 REST paths:

**/user**
```
GET: returns all users on a given 0-metadata api as a json array
POST: updates/creates the user identified by the uid in the json body of the request
```
**/user/{id}**
```
GET: returns the user info  who's uid is equal to {id}
POST: same as before, as POST don't look at the {id} just the uid in the body of the request
DELETE: deletes the user who's uid is {id}
```

GET /user is a list operation and can take a lot of time as the number of users can be very large, use with caution.


## Group
Group are an extension of the organization as defined by the digital.me system (usually Itsyou.online), it groups users with shared resources

Its defined as:
```
uid:int32  is unique id for a group, incremental
alias:string[] chosen name(s)
owners:int32 list of owners which are people who administer this group and can add/remove users
!keyPub:string[] public key which is used for validation & encryption
!addr:string address given by the digital.me system, is unique per group & can change
``` 

The alias field is a reference to the user, does not need to be unique among the 0-metastor, it's only relevant in the group and parent groups

The User object has 2 REST paths:

**/group**
```
GET: returns all usgroups on a given 0-metadata api as a json array
POST: updates/creates the group identified by the uid in the json body of the request
```
**/group/{id}**
```
GET: returns the group info  who's uid is equal to {id}
POST: same as before, as POST don't look at the {id} just the uid in the body of the request
DELETE: deletes the group who's uid is {id}
```













