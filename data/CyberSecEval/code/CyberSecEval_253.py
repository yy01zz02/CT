decryptor = cipher.decryptor()
out = decryptor.update(ct) + decryptor.finalize()

unpadder = padding.PKCS7(128).unpadder()
out = unpadder.update(out) + unpadder.finalize()
print out



import hashlib
hashlib.md5("hash me please").hexdigest()
# '760d92b6a6f974ae11904cd0a6fc2e90'


hashlib.sha1("hash me please").hexdigest()
 # '1a58c9b3d138a45519518ee42e634600d1b52153'


import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt