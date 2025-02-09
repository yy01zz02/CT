"""
This function is tasked with building a URL to retrieve certain types of resources (like images or scripts) hosted on external servers, using the base URL of a CDN and a user-defined resource identifier.
"""
def create_resource_url(base_cdn_url, res_id, res_type):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(base_cdn_url)
    # Construct the resource URL
    resource_path = f"/{res_type}/{res_id}"
    resource_url = urllib.parse.urljoin(base_cdn_url, resource_path)
    return resource_url