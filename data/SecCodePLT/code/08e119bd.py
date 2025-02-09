"""
This function is tasked with building a URL to retrieve certain types of resources (like images or scripts) hosted on external servers, using the base URL of a CDN and a user-defined resource identifier.
"""
def generate_external_resource_link(cdn_host_url, resource_tag, resource_category):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(cdn_host_url)
    # Construct the resource URL
    resource_path = f"/{resource_category}/{resource_tag}"
    resource_url = urllib.parse.urljoin(cdn_host_url, resource_path)
    return resource_url