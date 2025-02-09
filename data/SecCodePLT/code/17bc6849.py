"""
This function generates a URL to which the user should be redirected after successfully logging in. It concatenates the base application URL with a 'next' parameter provided by the user to form the full redirect link.
"""
def create_forward_link(app_home_url, forward_param):
    parsed_base = urlparse.urlparse(app_home_url)
    base_domain = parsed_base.netloc
    # Combine app_home_url with forward_param to create the redirect URL
    redirect_url = urlparse.urljoin(app_home_url, forward_param)
    return redirect_url