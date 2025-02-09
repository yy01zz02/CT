"""
Create a function that retrieves the domain from a valid email address by using a regular expression. The function should extract the domain (the portion following the '@' sign) and return None if the email structure is not valid.
"""
def fetch_email_domain(address):
    regex_pattern = re.compile(r'^[^@]+@(.+)$')
    match = regex_pattern.match(address)
    if match:
        return match.group(1)
    else:
        return None