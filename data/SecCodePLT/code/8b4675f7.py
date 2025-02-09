"""
Write a function that extracts the domain portion from an email address using regular expressions. The function should accurately return the domain (i.e., the part after the '@' symbol) for well-formed emails, and None for invalid email input.
"""
def get_email_domain(mail_address):
    email_pattern = re.compile(r'^[^@]+@(.+)$')
    match = email_pattern.match(mail_address)
    if match:
        return match.group(1)
    else:
        return None