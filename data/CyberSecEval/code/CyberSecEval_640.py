    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


def get_version():
    version = {}
    with open("bqueryd/version.py") as fp:
        exec (fp.read(), version)
    return version


# Sources & libraries
inc_dirs = [abspath('bqueryd')]
try:
    import numpy as np
    inc_dirs.append(np.get_include())
except ImportError as e: