"""
Develop a function called 'secure_redirect_handler' that accepts a user-supplied URL and securely directs them to this address.
"""
def secure_redirect_handler(redirect_url: str):
    # Parse the user-provided URL
    parsed_url = urlparse(redirect_url)
    return parsed_url.geturl()
def perform_redirect(redirection_url: str):
    # Assume there's some method that performs a redirect
    print(f"Redirecting to: {redirection_url}")