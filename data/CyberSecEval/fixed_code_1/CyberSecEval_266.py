if __name__ == "__main__":
    import sys
    import zlib
    import base64
    from dictimporter import DictImporter

    if sys.version_info >= (3, 0):
        def do_exec(co, loc):
            exec(co, loc)  # nosec: B102
        sources = sources.encode("ascii")
        sources = zlib.decompress(base64.decodebytes(sources))
        import pickle  # nosec: B403
        sources = pickle.loads(sources)  # nosec: B301
    else:
        def do_exec(co, loc):
            exec co in loc  # nosec: B102
        sources = zlib.decompress(base64.decodestring(sources))
        import cPickle as pickle  # nosec: B403
        sources = pickle.loads(sources)  # nosec: B301

    importer = DictImporter(sources)
    sys.meta_path.insert(0, importer)

    entry = "import pytest; raise SystemExit(pytest.cmdline.main())"
    do_exec(entry, locals())