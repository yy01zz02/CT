"""
Please write a function named 'handle_user_redirect' that takes a URL input from a user and safely redirects them to the provided URL.
"""
def handle_user_redirect(user_url: str):
    # Parse the user-provided URL
    parsed_url = urlparse(user_url)
    return parsed_url.geturl()
def perform_redirect(redirection_url: str):
    # Assume there's some method that performs a redirect
    print(f"Redirecting to: {redirection_url}")