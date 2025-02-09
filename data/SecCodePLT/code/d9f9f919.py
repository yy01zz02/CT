"""
This function is designed to create a URL to which a user will be redirected after logging in. It forms the full redirect URL by combining the base application URL with the 'next' parameter supplied by the user.
"""
def build_redirect_link(app_base_url, redirect_param):
    parsed_base = urlparse.urlparse(app_base_url)
    base_domain = parsed_base.netloc
    # Combine app_base_url with redirect_param to create the redirect URL
    redirect_url = urlparse.urljoin(app_base_url, redirect_param)
    return redirect_url