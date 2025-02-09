"""
This function creates a full redirect URL for API requests by combining the base API URL, a specific endpoint, and optional query parameters.
"""
def construct_redirect_url(main_url, endpoint_name, params_dict=None):
    # Parse the API base URL
    parsed_api_url = urllib.parse.urlparse(main_url)
    # Construct the API redirect URL
    redirect_url = urllib.parse.urljoin(main_url, endpoint_name)
    if params_dict:
        redirect_url += '?' + urllib.parse.urlencode(params_dict)
    return redirect_url