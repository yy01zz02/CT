                continue
            properties[key] = value

    image_meta['properties'] = properties

    return image_meta


def get_hash_str(base_str):
    """returns string that represents hash of base_str (in hex format)."""
    return hashlib.md5(base_str).hexdigest()

if hasattr(hmac, 'compare_digest'):
    constant_time_compare = hmac.compare_digest
else:
    def constant_time_compare(first, second):
        """Returns True if both string inputs are equal, otherwise False.

        This function should take a constant amount of time regardless of
        how many characters in the strings match.