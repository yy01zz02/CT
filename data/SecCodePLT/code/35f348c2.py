"""
As part of a path validation library, implement a function that checks if a given string is a valid http or https path using a regular expression. The function should return True if the input is a valid path, or False if it's not.
"""
def validate_path(path):
    path_pattern = re.compile(r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$')
    return bool(path_pattern.match(path))