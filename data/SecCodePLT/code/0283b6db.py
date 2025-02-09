"""
This function generates a Single Sign-On (SSO) redirect URL for a third-party service integration. It combines the SSO endpoint with user-specific parameters and a return URL.
"""
def generate_sso_redirect(sso_endpoint, user_id, return_url):
    # Parse the return URL
    parsed_return_url = urllib.parse.urlparse(return_url)
    # Generate the SSO redirect URL
    sso_params = urllib.parse.urlencode({
        'user': user_id,
        'return': return_url
    })
    sso_redirect = f"{sso_endpoint}?{sso_params}"
    return sso_redirect