
MOLD_DIMENSIONS = {"key1": None}


def setup_metrics(argv):

    for a in range(100):
        MOLD_DIMENSIONS['key1'] = (
            ''.join(random.sample(string.ascii_uppercase * 6, 6)))
        MOLD_DIMENSIONS['key2'] = (
            ''.join(random.sample(string.ascii_uppercase * 6, 6)))
        MOLD_DIMENSIONS['key_' + str(a)] = (
            ''.join(random.sample(string.ascii_uppercase * 6, 6)))

        """
        import hashlib
        key_str = json.dumps(MOLD_DIMENSIONS, sort_keys=True,
                             indent=None,
                             separators=(',', ':'))
