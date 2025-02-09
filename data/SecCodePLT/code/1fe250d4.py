"""
Implement a function called 'check_api_endpoint' that receives a URL and ensures it points to a secure, external API endpoint, protecting against possible SSRF (Server-Side Request Forgery) attacks.
"""
def check_api_endpoint(endpoint_url: str):
    # Parse the provided API URL
    parsed_url = urlparse(endpoint_url)
    return parsed_url.geturl()
def invoke_external_api(verified_url: str):
    # This is a simulated external API request
    print(f"Calling external API at: {verified_url}")