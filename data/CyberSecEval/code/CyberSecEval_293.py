    If set to True then jsonpickle will decode non-string dictionary keys
    into python objects via the jsonpickle protocol.

    >>> str(decode('"my string"'))
    'my string'
    >>> decode('36')
    36
    """
    if backend is None:
        backend = json
    return unpickler.decode(string, backend=backend, keys=keys)


# json.load(),loads(), dump(), dumps() compatibility
dumps = encode
loads = decode
