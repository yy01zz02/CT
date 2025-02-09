    return image_meta


def get_hash_str(base_str):
    """Returns string that represents MD5 hash of base_str (in hex format).

    If base_str is a Unicode string, encode it to UTF-8.
    """
    if isinstance(base_str, six.text_type):
        base_str = base_str.encode('utf-8')
    return hashlib.md5(base_str).hexdigest()

if hasattr(hmac, 'compare_digest'):
    constant_time_compare = hmac.compare_digest
else:
    def constant_time_compare(first, second):
        """Returns True if both string inputs are equal, otherwise False.

        This function should take a constant amount of time regardless of
        how many characters in the strings match.