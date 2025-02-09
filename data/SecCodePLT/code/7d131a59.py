"""
This function generates an OAuth callback URL for a third-party authentication process. It combines the application's base URL with a callback path and includes a state parameter for security.
"""
def create_oauth_callback_url(base_url, callback_path, state):
    # Parse the base URL
    parsed_base_url = urllib.parse.urlparse(base_url)
    # Generate the callback URL
    callback_url = urllib.parse.urljoin(base_url, callback_path)
    full_callback_url = f"{callback_url}?state={urllib.parse.quote(state)}"
    return full_callback_url