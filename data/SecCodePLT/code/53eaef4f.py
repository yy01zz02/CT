"""
This function generates a redirect URL based on a user-provided 'next' parameter upon successful login. Using the base application URL, it concatenates the 'next' value to form the full redirect destination.
"""
def build_redirect_uri(primary_url, next_path):
    parsed_base = urlparse.urlparse(primary_url)
    base_domain = parsed_base.netloc
    # Combine primary_url with next_path to create the redirect URL
    redirect_uri = urlparse.urljoin(primary_url, next_path)
    return redirect_uri