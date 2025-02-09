"""
This function builds an OAuth callback URL for third-party authentication by combining a base URL, the callback path, and a state parameter for securing the flow.
"""
def assemble_oauth_callback_url(root_url, path_for_callback, session_token):
    # Parse the base URL
    parsed_base_url = urllib.parse.urlparse(root_url)
    # Generate the callback URL
    callback_url = urllib.parse.urljoin(root_url, path_for_callback)
    full_callback_url = f"{callback_url}?state={urllib.parse.quote(session_token)}"
    return full_callback_url