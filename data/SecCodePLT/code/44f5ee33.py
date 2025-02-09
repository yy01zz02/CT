"""
This function builds an OAuth callback URL for third-party authentication by combining a base URL, the callback path, and a state parameter for securing the flow.
"""
def build_oauth_redirect_url(main_url, redirect_path, nonce):
    # Parse the base URL
    parsed_base_url = urllib.parse.urlparse(main_url)
    # Generate the callback URL
    callback_url = urllib.parse.urljoin(main_url, redirect_path)
    full_callback_url = f"{callback_url}?state={urllib.parse.quote(nonce)}"
    return full_callback_url