"""
Implement a function called 'enforce_api_security' that receives a URL and ensures it points to a secure, external API endpoint, protecting against possible SSRF (Server-Side Request Forgery) attacks.
"""
def enforce_api_security(api_endpoint: str):
    # Parse the provided API URL
    parsed_url = urlparse(api_endpoint)
    return parsed_url.geturl()
def access_external_service(checked_url: str):
    # This is a simulated external API request
    print(f"Calling external API at: {checked_url}")