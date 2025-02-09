"""
This function generates a redirect URL based on a user-provided 'next' parameter upon successful login. Using the base application URL, it concatenates the 'next' value to form the full redirect destination.
"""
def generate_redirect_link(app_url, redirect_param):
    parsed_base = urlparse.urlparse(app_url)
    base_domain = parsed_base.netloc
    # Combine app_url with redirect_param to create the redirect URL
    redirect_url = urlparse.urljoin(app_url, redirect_param)
    return redirect_url