"""
This function is responsible for assembling a URL to access resources stored on external servers, given a resource ID and the base URL of a CDN (Content Delivery Network). This mechanism is commonly used to retrieve files like images or JavaScript.
"""
def build_cdn_resource_url(cdn_url_base, file_id, file_type):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(cdn_url_base)
    # Construct the resource URL
    file_path = f"/{file_type}/{file_id}"
    complete_url = urllib.parse.urljoin(cdn_url_base, file_path)
    return complete_url