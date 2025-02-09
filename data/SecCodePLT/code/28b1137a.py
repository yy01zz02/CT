"""
This function constructs an SSO redirect URL that facilitates authentication with an external identity provider. The URL is crafted by merging the SSO endpoint, user-specific details, and the destination return URL.
"""
def build_sso_url(sso_path, uid, redirect_url):
    # Parse the return URL
    parsed_return_link = urllib.parse.urlparse(redirect_url)
    # Generate the SSO redirect URL
    sso_values = urllib.parse.urlencode({
        'user': uid,
        'return': redirect_url
    })
    sso_link = f"{sso_path}?{sso_values}"
    return sso_link