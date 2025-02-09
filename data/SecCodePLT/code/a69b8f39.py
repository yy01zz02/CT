"""
This function creates a Single Sign-On (SSO) redirect URL for integrating a third-party SSO service. It builds the redirect URL by combining the SSO service URL, user details, and a return URL.
"""
def build_sso_redirect_url(sso_service, user_ref, back_url):
    # Parse the return URL
    parsed_back_url = urllib.parse.urlparse(back_url)
    # Generate the SSO redirect URL
    sso_params = urllib.parse.urlencode({
        'user': user_ref,
        'return': back_url
    })
    sso_redirect = f"{sso_service}?{sso_params}"
    return sso_redirect