"""
This function is designed to build a redirect URL for Single Sign-On (SSO) authentication with a third-party provider. It combines the SSO endpoint, user ID, and a specified return URL.
"""
def construct_sso_redirect(auth_service_endpoint, user_identifier, redirect_uri):
    # Parse the return URL
    parsed_return_url = urllib.parse.urlparse(redirect_uri)
    # Generate the SSO redirect URL
    sso_params = urllib.parse.urlencode({
        'user': user_identifier,
        'return': redirect_uri
    })
    sso_redirect = f"{auth_service_endpoint}?{sso_params}"
    return sso_redirect