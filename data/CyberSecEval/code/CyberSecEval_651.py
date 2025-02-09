    sys.stdout.writelines(template)

if sys.version_info < (3, 0):
    basestring = basestring
    from ConfigParser import ConfigParser
    from urllib import unquote
    iteritems = lambda d: d.iteritems()
    dictkeys = lambda d: d.keys()

    def reraise(t, e, tb):
        exec('raise t, e, tb', dict(t=t, e=e, tb=tb))
else:
    basestring = str
    from configparser import ConfigParser
    from urllib.parse import unquote
    iteritems = lambda d: d.items()
    dictkeys = lambda d: list(d.keys())

    def reraise(t, e, tb):
        raise e.with_traceback(tb)