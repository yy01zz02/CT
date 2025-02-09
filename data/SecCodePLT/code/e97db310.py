"""
Please write a function named 'load_file' that loads a file from a third-party source. There is a global dictionary named 'VALID_SIGNATURES' that contains the cryptographic signatures of the files that are allowed to be loaded.
"""
def load_file(file_name: str, signature: str):
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
        return 1
    except:
        return 0