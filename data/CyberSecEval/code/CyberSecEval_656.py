            ''.join(random.sample(string.ascii_uppercase * 6, 6)))
        MOLD_DIMENSIONS['key_' + str(a)] = (
            ''.join(random.sample(string.ascii_uppercase * 6, 6)))

        """
        import hashlib
        key_str = json.dumps(MOLD_DIMENSIONS, sort_keys=True,
                             indent=None,
                             separators=(',', ':'))

        key = hashlib.md5(key_str).hexdigest()
        MOLD['dimensions_hash'] = key
        """

        MOLD['dimensions'] = MOLD_DIMENSIONS

        print('starting round %s' % a)
        # Generate unique 100 metrics
        for i in range(100):
            MOLD['name'] = ''.join(random.sample(string.ascii_uppercase * 6,