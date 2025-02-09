"""
This function constructs an SSO redirect URL that facilitates authentication with an external identity provider. The URL is crafted by merging the SSO endpoint, user-specific details, and the destination return URL.
"""
def create_sso_url(auth_endpoint, uid, redirect_url):
    # Parse the return URL
    parsed_redirect_url = urllib.parse.urlparse(redirect_url)
    # Generate the SSO redirect URL
    sso_params = urllib.parse.urlencode({
        'user': uid,
        'return': redirect_url
    })
    full_sso_url = f"{auth_endpoint}?{sso_params}"
    return full_sso_url