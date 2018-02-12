
def dirEqual(A,B):
    assert A.acl == B.acl
    assert A.bobjectItems == B.bobjectItems
    assert A.name == B.name
    assert A.secret == B.secret
    assert A.size == B.size
    assert A.uid == B.uid
    assert A.uidParent == B.uidParent
    assert posixEqual(A.posix,B.posix)
    # Arrays are sorted
    assert sorted(A.files) == sorted(B.files)
    assert sorted(A.linkItems) == sorted(B.linkItems)
    assert sorted(A.metadataItems) == sorted(B.metadataItems)
    assert sorted(A.specialItems) == sorted(B.specialItems)
    assert sorted(A.subdirs) == sorted(B.subdirs)
    return True

def posixEqual(A,B):
    assert A.mode == B.mode
    assert A.uname == B.uname
    assert A.gname == B.gname
    return True

def userEqual(A,B):
    assert A.addr == B.addr
    assert A.uid == B.uid
    # Arrays are sorted so comparison is fair
    assert sorted(A.alias) == sorted(B.alias)
    assert sorted(A.keyPub) == sorted(B.keyPub)
    return True

def groupEqual(A,B):
    assert userEqual(A,B)
    assert A.owners == B.owners
    return True

def aclEqual(A,B):
    assert A.uid == B.uid
    assert sorted(A.aci) == sorted(B.aci)
    assert A.hash == B.hash
    return True

def bdomainEqual(A,B):
    assert A.uid == B.uid
    assert A.id == B.id
    assert A.admins == B.admins
    assert A.author == B.author
    assert A.description == B.description
    assert A.moddate == B.moddate
    assert A.name == B.name
    assert A.signature == B.signature
    return True 