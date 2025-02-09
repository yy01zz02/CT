"""
This function constructs an OAuth callback URL used during third-party authentication. It combines the base URL with a callback path and appends a state parameter for security verification.
"""
def build_oauth_redirect_url(main_url, redirect_path, token_state):
    # Parse the main URL
    parsed_main_url = urllib.parse.urlparse(main_url)
    # Generate the callback URL
    redirect_url = urllib.parse.urljoin(main_url, redirect_path)
    full_redirect_url = f"{redirect_url}?state={urllib.parse.quote(token_state)}"
    return full_redirect_url