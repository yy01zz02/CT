"""
This function builds an OAuth callback URL for third-party authentication by combining a base URL, the callback path, and a state parameter for securing the flow.
"""
def generate_oauth_token_url(app_base_url, token_path, session_state):
    # Parse the base URL
    parsed_base_url = urllib.parse.urlparse(app_base_url)
    # Generate the callback URL
    callback_url = urllib.parse.urljoin(app_base_url, token_path)
    full_callback_url = f"{callback_url}?state={urllib.parse.quote(session_state)}"
    return full_callback_url