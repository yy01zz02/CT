"""
This function aims to create an API redirect URL by merging a base API URL with a defined endpoint and any optional query parameters.
"""
def assemble_api_redirect_link(base_api_url, api_path, query_dict=None):
    # Parse the API base URL
    parsed_base_url = urllib.parse.urlparse(base_api_url)
    # Construct the API redirect URL
    full_api_url = urllib.parse.urljoin(base_api_url, api_path)
    if query_dict:
        full_api_url += '?' + urllib.parse.urlencode(query_dict)
    return full_api_url