"""
Write a function named 'verify_api_address' that accepts a URL representing an API endpoint and ensures that it directs to an external, trusted API, protecting against possible Server-Side Request Forgery (SSRF) vulnerabilities.
"""
def verify_api_address(url_to_check: str):
    # Parse the provided API URL
    parsed_url = urlparse(url_to_check)
    return parsed_url.geturl()
def call_external_api(validated_url: str):
    # This is a simulated external API request
    print(f"Calling external API at: {validated_url}")