"""
This function generates a URL used to access resources stored externally, based on a given resource identifier and the CDN's base URL. These resources could include images, scripts, among others.
"""
def build_external_resource_link(cdn_url, resource_key, res_category):
    # Parse the CDN base URL
    parsed_cdn_url = urllib.parse.urlparse(cdn_url)
    # Construct the resource URL
    resource_path = f"/{res_category}/{resource_key}"
    resource_url = urllib.parse.urljoin(cdn_url, resource_path)
    return resource_url