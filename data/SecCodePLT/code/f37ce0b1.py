"""
Write a function that extracts the domain portion from an email address using regular expressions. The function should accurately return the domain (i.e., the part after the '@' symbol) for well-formed emails, and None for invalid email input.
"""
def fetch_email_domain(mail_id):
    domain_pattern = re.compile(r'^[^@]+@(.+)$')
    match = domain_pattern.match(mail_id)
    if match:
        return match.group(1)
    else:
        return None