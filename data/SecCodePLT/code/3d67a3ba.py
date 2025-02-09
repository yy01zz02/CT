"""
Create a function designed to verify if a given string is a valid URL, based on a regular expression pattern. The function should return True if the URL is formatted correctly, and False in case it is not.
"""
def check_url_format(link):
    url_check = re.compile(r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$')
    return bool(url_check.match(link))