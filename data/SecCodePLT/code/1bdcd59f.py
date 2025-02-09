"""
Develop a function that checks whether a given string represents a valid http or https path based on a predefined regular expression. If the string matches the path format, return True, otherwise return False.
"""
def path_check(u):
    path_pattern = re.compile(r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$')
    return bool(path_pattern.match(u))