"""
This function generates a URL used to access resources stored externally, based on a given resource identifier and the CDN's base URL. These resources could include images, scripts, among others.
"""
def generate_external_resource_url(cdn_base, res_id, res_type):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(cdn_base)
    # Construct the resource URL
    resource_path = f"/{res_type}/{res_id}"
    resource_url = urllib.parse.urljoin(cdn_base, resource_path)
    return resource_url