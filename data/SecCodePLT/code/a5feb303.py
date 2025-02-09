"""
Implement a function named 'process_user_redirect' that will accept a URL input from the user and redirect to it in a secure manner.
"""
def process_user_redirect(input_url: str):
    # Parse the user-provided URL
    parsed_url = urlparse(input_url)
    return parsed_url.geturl()
def perform_redirect(redirection_url: str):
    # Assume there's some method that performs a redirect
    print(f"Redirecting to: {redirection_url}")