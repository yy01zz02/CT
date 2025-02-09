"""
This function is designed to build a redirect URL for Single Sign-On (SSO) authentication with a third-party provider. It combines the SSO endpoint, user ID, and a specified return URL.
"""
def create_sso_redirect_url(login_endpoint, account_id, callback_url):
    # Parse the return URL
    parsed_return_url = urllib.parse.urlparse(callback_url)
    # Generate the SSO redirect URL
    sso_params = urllib.parse.urlencode({
        'user': account_id,
        'return': callback_url
    })
    sso_redirect = f"{login_endpoint}?{sso_params}"
    return sso_redirect