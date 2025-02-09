"""
The goal of this function is to generate a redirect URL for making API requests. It combines a specified base URL and endpoint, along with optional query parameters, into a complete redirect URL.
"""
def create_api_redirect_url(base_url_api, api_endpoint, opts=None):
    # Parse the API base URL
    parsed_api_url = urllib.parse.urlparse(base_url_api)
    # Construct the API redirect URL
    full_path = urllib.parse.urljoin(base_url_api, api_endpoint)
    if opts:
        full_path += '?' + urllib.parse.urlencode(opts)
    return full_path