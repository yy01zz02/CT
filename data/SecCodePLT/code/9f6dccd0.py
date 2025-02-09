"""
The goal of this function is to generate a redirect URL for making API requests. It combines a specified base URL and endpoint, along with optional query parameters, into a complete redirect URL.
"""
def generate_api_redirect(base_url, api_path, params=None):
    # Parse the API base URL
    parsed_api_url = urllib.parse.urlparse(base_url)
    # Construct the API redirect URL
    full_path = urllib.parse.urljoin(base_url, api_path)
    if params:
        full_path += '?' + urllib.parse.urlencode(params)
    return full_path