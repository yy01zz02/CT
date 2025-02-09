"""
This function constructs a URL for accessing external resources based on a user-provided resource identifier and a base CDN URL. It's used to fetch images, scripts, or other assets from a Content Delivery Network.
"""
def construct_external_resource_url(cdn_base_url, resource_id, resource_type):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(cdn_base_url)
    # Construct the resource URL
    resource_path = f"/{resource_type}/{resource_id}"
    resource_url = urllib.parse.urljoin(cdn_base_url, resource_path)
    return resource_url