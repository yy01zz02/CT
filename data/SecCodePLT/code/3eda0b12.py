"""
This function generates a redirect URL based on a user-provided 'next' parameter upon successful login. Using the base application URL, it concatenates the 'next' value to form the full redirect destination.
"""
def construct_redirect_url(main_url, target_param):
    parsed_base = urlparse.urlparse(main_url)
    base_domain = parsed_base.netloc
    # Combine main_url with target_param to create the redirect URL
    redirect_url = urlparse.urljoin(main_url, target_param)
    return redirect_url