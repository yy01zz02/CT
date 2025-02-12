# Load filters with tests we should skip

#=========================================================================

py_test_accept_filter = None





def _load_filters():

    global py_test_accept_filter

    if py_test_accept_filter is None:

        py_test_accept_filter = os.environ.get('PYDEV_PYTEST_SKIP')

        if py_test_accept_filter:

            py_test_accept_filter = json.loads(

                zlib.decompress(base64.b64decode(py_test_accept_filter)).decode('utf-8'))



            if Path is not None:

                # Newer versions of pytest resolve symlinks, so, we

                # may need to filter with a resolved path too.

                new_dct = {}

                for filename, value in py_test_accept_filter.items():

                    new_dct[canonical_normalized_path(str(Path(filename).resolve()))] = value