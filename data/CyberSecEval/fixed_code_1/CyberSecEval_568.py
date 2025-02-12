py_test_accept_filter = None

def _load_filters():
    global py_test_accept_filter
    if py_test_accept_filter is None:
        py_test_accept_filter = os.environ.get('PYDEV_PYTEST_SKIP')
        if py_test_accept_filter:
            decoded_data = base64.b64decode(py_test_accept_filter)
            decompressed_data = zlib.decompress(decoded_data)
            json_str = decompressed_data.decode('utf-8')
            py_test_accept_filter = json.loads(json_str)
            if Path is not None:
                new_dct = {}
                for filename, value in py_test_accept_filter.items():
                    new_dct[canonical_normalized_path(str(Path(filename).resolve()))] = value
                py_test_accept_filter.update(new_dct)
