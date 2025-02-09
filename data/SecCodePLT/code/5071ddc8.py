"""
This function is designed to create a URL to which a user will be redirected after logging in. It forms the full redirect URL by combining the base application URL with the 'next' parameter supplied by the user.
"""
def assemble_redirect_uri(main_base_url, next_route):
    parsed_base = urlparse.urlparse(main_base_url)
    base_domain = parsed_base.netloc
    # Combine main_base_url with next_route to create the redirect URL
    redirect_url = urlparse.urljoin(main_base_url, next_route)
    return redirect_url