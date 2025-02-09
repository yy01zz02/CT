import tempfile


def write_results(results):
    '''
        Create a temporary file with UTF-8 encoding,
        write the unicode string results to it,
        and return its path.
    '''
    with tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8', delete=False) as tmp_file:
        tmp_file.write(results)
        filename = tmp_file.name
    return filename