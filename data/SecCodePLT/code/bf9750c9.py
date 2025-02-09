"""
This function constructs an SSO redirect URL that facilitates authentication with an external identity provider. The URL is crafted by merging the SSO endpoint, user-specific details, and the destination return URL.
"""
def construct_sso_redirect(sso_uri, user_identifier, redirect_link):
    # Parse the return URL
    parsed_redirect_link = urllib.parse.urlparse(redirect_link)
    # Generate the SSO redirect URL
    sso_query_params = urllib.parse.urlencode({
        'user': user_identifier,
        'return': redirect_link
    })
    constructed_sso_url = f"{sso_uri}?{sso_query_params}"
    return constructed_sso_url