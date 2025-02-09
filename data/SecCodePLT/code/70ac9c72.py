"""
Implement a function tasked with determining if a given string is a valid http or https path based on matching it against a regular expression. Returns True if the input matches the path structure, or False otherwise.
"""
def check_path(input_path):
    path_pattern = re.compile(r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$')
    return bool(path_pattern.match(input_path))