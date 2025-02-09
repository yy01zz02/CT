"""
This function constructs an OAuth callback URL used during third-party authentication. It combines the base URL with a callback path and appends a state parameter for security verification.
"""
def generate_oauth_callback_link(app_base_url, callback_endpoint, verification_state):
    # Parse the base URL
    parsed_base_url = urllib.parse.urlparse(app_base_url)
    # Generate the callback URL
    callback_url = urllib.parse.urljoin(app_base_url, callback_endpoint)
    full_callback_url = f"{callback_url}?state={urllib.parse.quote(verification_state)}"
    return full_callback_url