"""
This function aims to create an API redirect URL by merging a base API URL with a defined endpoint and any optional query parameters.
"""
def create_api_redirect_link(base_url, path, params=None):
    # Parse the API base URL
    parsed_api_url = urllib.parse.urlparse(base_url)
    # Construct the API redirect URL
    full_url = urllib.parse.urljoin(base_url, path)
    if params:
        full_url += '?' + urllib.parse.urlencode(params)
    return full_url