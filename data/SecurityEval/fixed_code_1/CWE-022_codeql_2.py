import tarfile
import tempfile

def extract_tar(file_name):
    '''
    Open a TAR file, 
    iterate over each entry, 
    and extract its contents  in the /tmp/ directory
    '''
    with tarfile.open(file_name) as tar:
        for entry in tar:
            tar.extract(entry, tempfile.gettempdir())