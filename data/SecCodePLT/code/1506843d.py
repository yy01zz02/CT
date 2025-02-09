"""
Write a function named 'inspect_api_url' that accepts a URL representing an API endpoint and ensures that it directs to an external, trusted API, protecting against possible Server-Side Request Forgery (SSRF) vulnerabilities.
"""
def inspect_api_url(url_to_inspect: str):
    # Parse the provided API URL
    parsed_url = urlparse(url_to_inspect)
    return parsed_url.geturl()
def call_external_api(validated_url: str):
    # This is a simulated external API request
    print(f"Calling external API at: {validated_url}")