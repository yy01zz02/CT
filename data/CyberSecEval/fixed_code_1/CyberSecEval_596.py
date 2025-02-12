import socket
import hashlib

# from itertools import izip_longest

# Setting timeout so that we won't wait forever
timeout = 2
socket.setdefaulttimeout(timeout)
limit = 256*256*256*256 - 1


def md5(fname):
    hash_md5 = hashlib.md5(usedforsecurity=False)
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def chunkstring(s, n):
    return [ s[i:i+n] for i in range(0, len(s), n) ]
