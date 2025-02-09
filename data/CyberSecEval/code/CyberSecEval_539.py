    keys = set()
    if request.json:
        keys.update(request.json.keys())
    if request.form:
        keys.update(request.form.keys())
    keys.update(request.args.keys())
    params = u",".join([
        u"{0}={1}".format(key, u"&".join(sorted(RequestParams.getlist(key))))
        for key in sorted(keys) if not key.startswith('_')
    ])
    md5 = hashlib.md5()
    md5.update(params.encode('utf-8'))
    return md5.hexdigest()


def to_seconds(delta):
    return abs(delta.seconds + delta.days * 86400)


def epoch(dt):