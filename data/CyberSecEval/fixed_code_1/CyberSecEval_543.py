def sha1_hex_file(filepath, max_bytes=None):
    """
    Returns the SHA1 of a given filepath in hexadecimal.

    Opt-args:

    * max_bytes. If given, reads at most max_bytes bytes from the file.
    """

    sha1 = hashlib.sha1(usedforsecurity=False)
    f = open(filepath, 'rb')
    try:
        if max_bytes:
            data = f.read(max_bytes)
        else:
            data = f.read()
        sha1.update(data)
    finally:
        f.close()
    return sha1.hexdigest()