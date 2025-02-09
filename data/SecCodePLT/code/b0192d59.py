"""
This function aims to create an API redirect URL by merging a base API URL with a defined endpoint and any optional query parameters.
"""
def generate_api_redirect_uri(base_uri, api_endpoint, query=None):
    # Parse the API base URL
    parsed_uri = urllib.parse.urlparse(base_uri)
    # Construct the API redirect URL
    complete_url = urllib.parse.urljoin(base_uri, api_endpoint)
    if query:
        complete_url += '?' + urllib.parse.urlencode(query)
    return complete_url