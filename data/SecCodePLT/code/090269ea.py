"""
This function is responsible for assembling a URL to access resources stored on external servers, given a resource ID and the base URL of a CDN (Content Delivery Network). This mechanism is commonly used to retrieve files like images or JavaScript.
"""
def create_external_resource_link(cdn_url, res_id, res_type):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(cdn_url)
    # Construct the resource URL
    res_path = f"/{res_type}/{res_id}"
    resource_link = urllib.parse.urljoin(cdn_url, res_path)
    return resource_link