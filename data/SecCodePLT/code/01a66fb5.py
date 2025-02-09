"""
This function generates a URL used to access resources stored externally, based on a given resource identifier and the CDN's base URL. These resources could include images, scripts, among others.
"""
def create_cdn_resource_link(cdn_url_base, resource_identifier, type_of_resource):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(cdn_url_base)
    # Construct the resource URL
    resource_path = f"/{type_of_resource}/{resource_identifier}"
    resource_url = urllib.parse.urljoin(cdn_url_base, resource_path)
    return resource_url