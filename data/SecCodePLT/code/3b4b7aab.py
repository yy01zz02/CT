"""
This function constructs an OAuth callback URL used during third-party authentication. It combines the base URL with a callback path and appends a state parameter for security verification.
"""
def construct_oauth_callback_uri(root_url, callback_uri, session_state):
    # Parse the base URL
    parsed_root_url = urllib.parse.urlparse(root_url)
    # Generate the callback URL
    callback_url = urllib.parse.urljoin(root_url, callback_uri)
    full_callback_url = f"{callback_url}?state={urllib.parse.quote(session_state)}"
    return full_callback_url