"""
This function is responsible for assembling a URL to access resources stored on external servers, given a resource ID and the base URL of a CDN (Content Delivery Network). This mechanism is commonly used to retrieve files like images or JavaScript.
"""
def generate_cdn_content_url(cdn_origin_url, content_id, content_kind):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(cdn_origin_url)
    # Construct the resource URL
    content_path = f"/{content_kind}/{content_id}"
    complete_url = urllib.parse.urljoin(cdn_origin_url, content_path)
    return complete_url