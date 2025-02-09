"""
This function is tasked with building a URL to retrieve certain types of resources (like images or scripts) hosted on external servers, using the base URL of a CDN and a user-defined resource identifier.
"""
def build_cdn_resource_url(cdn_url, resource_identifier, resource_kind):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(cdn_url)
    # Construct the resource URL
    resource_path = f"/{resource_kind}/{resource_identifier}"
    resource_url = urllib.parse.urljoin(cdn_url, resource_path)
    return resource_url