"""
Create a function that retrieves the domain from a valid email address by using a regular expression. The function should extract the domain (the portion following the '@' sign) and return None if the email structure is not valid.
"""
def get_email_domain(email_addr):
    email_pattern = re.compile(r'^[^@]+@(.+)$')
    match = email_pattern.match(email_addr)
    if match:
        return match.group(1)
    else:
        return None