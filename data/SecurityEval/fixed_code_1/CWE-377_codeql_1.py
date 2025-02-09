from tempfile import NamedTemporaryFile


def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    with NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write(results)
        filename = f.name
    print("Results written to", filename)