"""
Design a function that utilizes regular expressions to extract the domain portion of a given email address. If the email address is correctly structured, the function should return the part that follows the '@' character. Otherwise, it should return None.
"""
def fetch_email_domain(email_addr):
    email_pattern = re.compile(r'^[^@]+@(.+)$')
    match = email_pattern.match(email_addr)
    if match:
        return match.group(1)
    else:
        return None