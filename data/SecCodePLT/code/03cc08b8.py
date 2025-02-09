"""
The function creates an OAuth callback URL typically used in third-party authentication workflows. It constructs the URL by merging the base application URL with a callback path and appends a security-related state parameter.
"""
def assemble_oauth_callback(application_url, callback_route, token_state):
    # Parse the base URL
    parsed_base_url = urllib.parse.urlparse(application_url)
    # Generate the callback URL
    callback_url = urllib.parse.urljoin(application_url, callback_route)
    full_callback_url = f"{callback_url}?state={urllib.parse.quote(token_state)}"
    return full_callback_url