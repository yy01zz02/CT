

def _make_hash(attrs):
    attrs = tuple(
        a
        for a in attrs
        if a.hash is True or (a.hash is None and a.cmp is True)
    )

    # We cache the generated hash methods for the same kinds of attributes.
    sha1 = hashlib.sha1()
    sha1.update(repr(attrs).encode("utf-8"))
    unique_filename = "<attrs generated hash %s>" % (sha1.hexdigest(),)
    type_hash = hash(unique_filename)
    lines = [
        "def __hash__(self):",
        "    return hash((",
        "        %d," % (type_hash,),
    ]
    for a in attrs: