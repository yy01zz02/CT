"""
As part of an email validation library, implement a function that extracts the domain part from an email address using a regular expression. The function should return the domain (everything after the '@' symbol) if the input is a valid email address, or None if it's not.
"""
def extract_email_domain(email):
    email_pattern = re.compile(r'^[^@]+@(.+)$')
    match = email_pattern.match(email)
    if match:
        return match.group(1)
    else:
        return None