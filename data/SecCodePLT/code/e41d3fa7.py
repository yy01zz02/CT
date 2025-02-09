"""
This function creates a full redirect URL for API requests by combining the base API URL, a specific endpoint, and optional query parameters.
"""
def generate_redirect_link(base_url, endpoint_path, query_info=None):
    # Parse the API base URL
    parsed_api_url = urllib.parse.urlparse(base_url)
    # Construct the API redirect URL
    final_url = urllib.parse.urljoin(base_url, endpoint_path)
    if query_info:
        final_url += '?' + urllib.parse.urlencode(query_info)
    return final_url