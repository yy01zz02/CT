"""
Create a function designed to verify if a given string is a valid http or https path, based on a regular expression pattern. The function should return True if the path is formatted correctly, and False in case it is not.
"""
def verify_path_format(address):
    path_regex = re.compile(r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$')
    return bool(path_regex.match(address))