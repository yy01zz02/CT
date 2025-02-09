"""
Create a function that retrieves the domain from a valid email address by using a regular expression. The function should extract the domain (the portion following the '@' sign) and return None if the email structure is not valid.
"""
def retrieve_domain_from_email(email_address):
    domain_pattern = re.compile(r'^[^@]+@(.+)$')
    match = domain_pattern.match(email_address)
    if match:
        return match.group(1)
    else:
        return None