        num /= 1000.0
    return "%.1f%s" % (num, "YB")


def gethash(filename, hash_function):
    """Calculates the hashvalue of the given file with the given hash_function.

    Args:
      filename: The file name to calculate the hash value of.
      hash_function: The hash function object to use, which was instantiated
          before calling this function, e.g. hashlib.md5().

    Returns:
      The hashvalue of the given file as hex string.
    """
    if not os.path.isfile(filename):
        return "NOT A FILE"

    fileref = open(filename, "rb")
    while 1: