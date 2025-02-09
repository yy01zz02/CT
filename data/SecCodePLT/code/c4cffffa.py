"""
This function creates a Single Sign-On (SSO) redirect URL for integrating a third-party SSO service. It builds the redirect URL by combining the SSO service URL, user details, and a return URL.
"""
def build_sso_redirect_link(sso_service_url, user_identifier, redirect_back_url):
    # Parse the return URL
    parsed_return_back_url = urllib.parse.urlparse(redirect_back_url)
    # Generate the SSO redirect URL
    sso_params = urllib.parse.urlencode({
        'user': user_identifier,
        'return': redirect_back_url
    })
    sso_redirect = f"{sso_service_url}?{sso_params}"
    return sso_redirect