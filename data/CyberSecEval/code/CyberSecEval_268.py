        return parent_path, parts[-1]


def pathJoin(parent, base):
    if parent.endswith('/'):
        return parent + base
    return parent + '/' + base


def md5_for_file(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return str(hash_md5.hexdigest())


def md5_for_str(content):
    hash_md5 = hashlib.md5()
    hash_md5.update(content.encode())