"""
This function creates a full redirect URL for API requests by combining the base API URL, a specific endpoint, and optional query parameters.
"""
def create_redirect_url(base_url_api, desired_endpoint, optional_params=None):
    # Parse the API base URL
    parsed_api_url = urllib.parse.urlparse(base_url_api)
    # Construct the API redirect URL
    constructed_url = urllib.parse.urljoin(base_url_api, desired_endpoint)
    if optional_params:
        constructed_url += '?' + urllib.parse.urlencode(optional_params)
    return constructed_url