    return is_str_none_or_whitespace(s) or is_str_none_or_whitespace(s.rstrip(' \t\r\n\0'))


def hash_strings(string_list):
    """
    Compute a cryptographic hash of a list of strings

    :param string_list: The strings to be hashed
    :return: The cryptographic hash (digest) of the strings in the order provided
    """
    sha1_hash = hashlib.sha1()
    for item in string_list:
        sha1_hash.update(item.encode())
    return sha1_hash.digest()


def format_memory_value(unit, value):
    units = {'bytes': 1, 'kilobytes': 1024, 'megabytes': 1024*1024, 'gigabytes': 1024*1024*1024}

    if unit not in units: