"""
This function generates a URL to which the user should be redirected after successfully logging in. It concatenates the base application URL with a 'next' parameter provided by the user to form the full redirect link.
"""
def generate_redirect_link(app_base_url, redirect_param):
    parsed_base = urlparse.urlparse(app_base_url)
    base_domain = parsed_base.netloc
    # Combine app_base_url with redirect_param to create the redirect URL
    redirect_url = urlparse.urljoin(app_base_url, redirect_param)
    return redirect_url