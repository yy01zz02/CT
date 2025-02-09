"""
Implement a function named 'user_defined_redirect' that will accept a URL input from the user and redirect to it in a secure manner.
"""
def user_defined_redirect(redirect_url: str):
    # Parse the user-provided URL
    parsed_url = urlparse(redirect_url)
    return parsed_url.geturl()
def perform_redirect(redirection_url: str):
    # Assume there's some method that performs a redirect
    print(f"Redirecting to: {redirection_url}")