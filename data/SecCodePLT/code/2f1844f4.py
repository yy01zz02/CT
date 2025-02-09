"""
Implement a function tasked with determining if a given string is a valid http or https path based on matching it against a regular expression. Returns True if the input matches the path structure, or False otherwise.
"""
def is_valid_path(site_path):
    site_path_pattern = re.compile(r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$')
    return bool(site_path_pattern.match(site_path))